# Fires of December — primary-text connection audit

Audit date: October 20, 2026. This report supersedes preview-only and forum-only descriptions of Fires coverage. The site contains the findings, not a copy of any uploaded book.

## What was actually checked

The user supplied Amazon EPUB content under a ZIP extension. ZIP integrity and EPUB structure passed. The Fires spine contains all 43 numbered chapters and the epilogue; these contain approximately 109,431 extracted words. The text was indexed in spine order, retaining chapter and internal-section locators. File numbers are not chapter numbers: illustrations split some chapters across several XHTML files.

This was a **systematic full-text search with contextual verification of connection candidates**, not a line-by-line literary reread. Broad searches covered characters, worlds, Invested arts, materials, entities, metaphysical terms and known crossover vocabulary across every chapter and the epilogue. A narrower named-reference search and a rare-capitalized-word inventory supplied additional candidates. Searches produced leads, not automatic confirmations. Selected relevant passages were read in context and reconciled with every pre-existing Fires claim. A chapter inventory and the resulting claim register are in [the audit ledger](audits/fires-2026-10-20.json).

Relevant comparison passages were checked in the supplied Tress, Yumi, The Sunlit Man and Isles of the Emberdark editions. Those four novels were not each given a complete independent audit. Only a few of the uploaded Wind and Truth sections have been inspected, so this is **not** a completed Wind and Truth audit. Warbreaker, the Mistborn trilogy, Shadows for Silence and Rhythm of War have not been supplied here; their side of a connection still uses established context and existing references rather than a new full-text check.

The “Less a Sword, More a Spike” illustration was inspected. The geometric symbol is visible; identifying it specifically as Reo continues to rely on the cited Coppermind identification. No assertion is made that every illustration, map, premium-edition extra, annotation or interview has been audited. Subtle unnamed allusions can still be missed by this method.

## Findings and corrections

| Connection or detail | Verified locator | Result |
| --- | --- | --- |
| Scadrial's canals | Fires III | Explicit world/historical reference; added. |
| Ironeyes | Fires VII | Narrator's death epithet; added as an allusion, not a Marsh cameo. |
| Doug and Doug | Fires VII; Tress XIV, “The Dougs” | Recurring narrative joke; added without equating the sailors with Tress's crew. |
| T'Telir's Court of Gods | Fires IX | Explicit Warbreaker place comparison; added. Audience nationality remains a theory. |
| Emotional dampening | Fires XXIV | Narrator explicitly compares the river's effect with Soothing; added without calling it brass Allomancy. |
| Scadrian garment | Fires XXIV | World comparison verified; exact garment remains unknown. |
| Negative-Investiture body and blood | Fires XXIV | Mechanism checked; the blood is not established as Dor. |
| Spike construction | Fires XXVI–XXVII, XXXVIII | Bind point, silver, Aon, modified power and their distinct functions checked. Preserve “Hemalurgy-adjacent.” |
| Aon versus Reo | Fires XXVII; XXVI illustration | Aon is named in prose; Reo is an artwork identification. Split into separate claims. |
| Godsflame and Ashyn | Fires XXVII; Epilogue | Hoid's identification and his stated surprise checked. Temple trap revealed later; exact origin/mechanism remains open. |
| Hoid's memory backups | Fires XXVII | Open-ended earlier incidents, **not exactly two**. Candidate matches remain theories. |
| Returned and Herald terminology | Fires XXVII | Added as terms Hoid denies for his condition; neither creates a cameo. Creed Wraith is also named, without a fabricated book identity. |
| Zuhel | Fires XXVII; XXXIV, XXXVII, XLII | Name and bond behavior checked. A universal one-bond-per-Realm model is not proved. |
| Luhel comparison | Tress XXXI, “The Midnight Essence” | Luhel and its contrast with Nahel checked directly. |
| Silver across systems | Fires XXVI, XXXVIII; Tress I, VIII, XXXI | Both books checked; effects differ. No universal magic-cancellation rule. |
| Transformed Breaths | Fires XXVII, XXXVIII; Epilogue | Initial hypothesis distinguished from later explanation; purified buffer and passphrase operations checked. |
| The Prophet's identity | Existing FanX 2026 confirmation; Fires XLI, Epilogue | Novel does not name him Vasher. Keep author confirmation as the identity source. |
| The Prophet's later activity | Fires XLI, Epilogue | Dream, Roshar confinement and remote simulacrum added. Distinct from his historical visit. |
| Design | Fires XXXVIII; Yumi V and “Another Epilogue” | Named mention added; she is away on an unexplained quest, not on-page in Fires. |
| Excessive sunrise | Fires XXXVIII; Sunlit Man I–II | Strong Canticle candidate; planet is unnamed in Fires, so identification stays optional theory. |
| Demonstone and sunhearts | Fires XXVI; Sunlit Man XII | Both passages checked. Functional analogy does not establish identical technology. |
| Ambitional entity family | Fires XXIV, XXVII; Emberdark XXV, XXXVI, XXXIX | Shared terminology checked; Megalith, Dakwara and encountered entity are not one individual. |
| Sixth Word | Fires XLI | Stated purpose checked. Origin and mechanics undisclosed; no Dawnshard identity assigned. |
| Final soul-sharing | Fires XLII | Added qualification: outcome is exceptional, not proof of how every Zuhel bond works. |
| Dragon helper | Fires XXVI | Explicitly separate from Prophet and Valor. Identity unknown. |
| Jasper and Tzendish cult | Fires IV, XXXVIII | Added unpaired references. No unsupported connection to a published book. |
| Killing God / collapse of reality | Fires IV, XXIII | Preserved narrator's statements; no invented second cosmological catastrophe. |
| Valor's activities | Fires IV, XXVII, Epilogue | Work on Miral, search and trap checked. Medelantorius is not named in the supplied text. |
| December’s translated name | Fires I; Postscript | Local name Hodołnika; author’s birth-month inspiration. No Earth-calendar inference. |
| Three dragon-ruled worlds | Fires Epilogue | Search clue added; worlds are unnamed. |

## Interpretation and chronology safeguards

The earlier assertion that December's story necessarily precedes Tress and Yumi was not established by these passages and has been removed. Historical visits, events experienced in possible futures, story time and narration time must remain distinct. Roshar is explicit; an exact absolute date is not established by this audit. The Prophet remembers the dream interaction in the epilogue, which deserves preservation without treating the entire possible-future experience as an ordinary past event.

The Yumi closing scene explicitly discusses Hoid's protection protocols after stolen memories; it does not establish which aside in Fires refers to which event. A proposed Rhythm of War or Wind and Truth match is still an interpretation. Likewise, the artwork's Aon identification, a guessed dragon, the audience's nationality, the sunrise's unnamed planet and the river's alleged Dor identity must not all inherit one generic “confirmed” label.

## Implementation and handoff

`data/curation.json` remains the editable source. Nested claims carry separate evidence, locators, citations and occasional short excerpts. `text-verified` means the stated passage was checked; it does not promote nearby theories to facts. Official book-reference URLs are clearly labeled as reference links, not public links to the user's uploaded text. Original research references remain available alongside the primary-text citations.

The site retains opt-in theories, spoiler reveals, stable progress IDs and the separate prerequisite graph. Do not replace this overlay with upstream-only data. Raw books, extracted text and inspected art stay outside the repository; none is to be committed or deployed. The audit ledger stores edition fingerprints, counts and paraphrased findings only.
