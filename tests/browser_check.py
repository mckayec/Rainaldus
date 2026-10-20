from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT=Path(__file__).resolve().parents[1]
(ROOT/'work').mkdir(exist_ok=True)
class Quiet(SimpleHTTPRequestHandler):
 def log_message(self,*args): pass
server=ThreadingHTTPServer(('127.0.0.1',0),partial(Quiet,directory=str(ROOT/'site')))
Thread(target=server.serve_forever,daemon=True).start()
url=f'http://127.0.0.1:{server.server_port}/'
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox'])
 page=browser.new_page(viewport={'width':1440,'height':1000})
 page.emulate_media(reduced_motion='reduce')
 errors=[]
 page.set_default_timeout(8000)
 page.on('pageerror',lambda e:errors.append(str(e)))
 page.route('https://fonts.googleapis.com/**',lambda r:r.abort())
 page.goto(url+'?case=mb2#mb2')
 page.wait_for_selector('#dossier-inner .d-title')
 assert 'Mistborn: The Final Empire' in page.locator('.alert').inner_text()
 assert not page.locator('.evidence-card').count()
 page.goto(url+'?case=iote#iote')
 page.wait_for_selector('#dossier-inner .d-title')
 assert 'optional' in page.locator('.reading-note').first.inner_text().lower()
 assert not page.locator('.connection-visual').count()
 assert not page.locator('.evidence-sources').count()
 page.locator('[data-reveal="tress>iote"]').click()
 assert page.locator('.connection-visual svg').count()==1
 assert 'Xisis' in page.locator('.evidence-card').inner_text()
 assert page.locator('.evidence-card a').count()>=2
 assert page.locator('.connection-visual svg').get_attribute('aria-label').startswith('Tress')
 page.locator('[data-reveal="book:iote"]').click()
 assert page.get_by_text('Official standalone book art gallery',exact=True).count()==1
 page.screenshot(path=str(ROOT/'work/emberdark-evidence-desktop.png'),full_page=True)
 # Saved reading state survives reload.
 page.locator('[data-read="iote"]').click()
 page.reload()
 page.wait_for_selector('.readbtn')
 assert page.locator('.readbtn').get_attribute('aria-pressed')=='true'
 # Exercise new/expanded dossiers and their evidence in both connection directions.
 page.evaluate("localStorage.setItem('cro.prefs', JSON.stringify({showPlanned:true,showExtras:true,conn:{egg:true}}))")
 # Published Fires must appear even with planned books hidden.
 page.evaluate("localStorage.setItem('cro.prefs', JSON.stringify({showPlanned:false}))")
 page.goto(url+'?check=fires-default#map')
 page.wait_for_selector('.map .node')
 assert page.locator('.map .node[data-id="fod"]').count()==1
 page.evaluate("localStorage.setItem('cro.prefs', JSON.stringify({showPlanned:true,showExtras:true,conn:{egg:true}}))")
 for book in ['sa5','elsecaller','lopen','dsp','twokp','fod']:
  page.goto(url+'?loop='+book+'#'+book)
  page.wait_for_selector('#dossier-inner .d-title')
  assert page.locator('.d-title').inner_text()
  while page.locator('[data-reveal]').count(): page.locator('[data-reveal]').first.click()
  assert page.locator('.coverage-note').count()==1
 page.goto(url+'?check=preview#fod')
 page.wait_for_selector('.d-title')
 assert 'Selected connections reviewed' in page.locator('.coverage-note').inner_text()
 assert page.locator('[data-show="showTheories"]').get_attribute('aria-checked')=='false'
 page.locator('[data-reveal="wb>fod"]').click()
 assert 'Author confirmed' in page.locator('#dossier-inner').inner_text()
 assert 'A Nalthian audience?' not in page.locator('#dossier-inner').inner_text()
 page.locator('[data-show="showTheories"]').click()
 assert page.locator('[data-show="showTheories"]').get_attribute('aria-checked')=='true'
 assert 'A Nalthian audience?' in page.locator('#dossier-inner').inner_text()
 assert 'Interpretation / open theory; unconfirmed' in page.locator('#dossier-inner').inner_text()
 page.locator('[data-show="showTheories"]').click()
 assert page.locator('.readbtn').count()==1
 page.locator('.readbtn').click()
 assert page.locator('.readbtn').get_attribute('aria-pressed')=='true'
 page.locator('[data-reveal="book:fod"]').click()
 assert page.locator('blockquote').count()==1
 # Prime drafts and their graph connections disappear with the toggle.
 page.goto(url+'?case=map#map')
 page.wait_for_selector('.map .node')
 assert page.locator('.map .node').count()==83
 assert page.locator('.map .node[data-id="dsp"]').count()==1
 page.locator('[data-show="showExtras"]').click()
 assert page.locator('.map .node[data-id="dsp"]').count()==0
 assert page.locator('.map [data-from="dsp"]').count()==0
 # Keyboard accessible reveal on a small screen; timeline leaves unknown works unplaced.
 page.set_viewport_size({'width':390,'height':844})
 page.goto(url+'?check=mobile#iote')
 page.wait_for_selector('.d-title')
 page.locator('[data-reveal="tress>iote"]').focus()
 page.keyboard.press('Enter')
 assert page.locator('.connection-visual').count()==1
 assert page.evaluate('document.documentElement.scrollWidth <= innerWidth')
 page.locator('.connection-visual').scroll_into_view_if_needed()
 assert page.locator('.connection-visual').is_visible()
 page.screenshot(path=str(ROOT/'work/emberdark-evidence-mobile.png'),full_page=True,animations='disabled')
 page.goto(url+'?case=path#path')
 page.wait_for_selector('#sort')
 page.locator('#sort').select_option('chronology')
 assert page.get_by_text('Not placed in this order',exact=True).count()==1
 assert page.locator('.row[data-id="fod"]').count()==1
 assert not errors,errors
 print('PASS: desktop/mobile evidence, spoiler gates, citations, original diagrams, saved progress, draft toggle, selected coverage, theory toggle, keyboard reveals, unknown timeline, no JS errors')
 browser.close()
server.shutdown()
