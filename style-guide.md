# Style guide

Genre: national/industry policy blue paper — a strategy document with case studies, tables and footnotes,
read by international policy analysts, open source practitioners, and industry readers.

## Audience and voice

- Audience: non-Chinese readers who know open source and AI, but not Chinese policy vocabulary or
  domestic platforms. Everything China-specific must be intelligible without a glossary at hand.
- Voice: third person, present tense for current state, past tense for history. Formal and neutral.
- The source is argumentative and slogan-heavy; keep the argument (and the criticism, including of
  Chinese actors), drop the sloganeering. No exclamation marks, no marketing adjectives the source
  does not have.
- Do not soften or strengthen claims. 面临若干关键瓶颈 stays "faces several critical bottlenecks",
  not "faces some challenges".

## Terminology

- The glossary is binding: one rendering per term for the whole book, no synonyms for variety.
- Chinese policy terms with a settled English equivalent use it (自主可控, 卡脖子, 耐心资本, 规上企业 —
  see the glossary notes). Where the glossary lists alternatives in a note, the choice is already made
  in the `en` column; flag any you disagree with in the review reply rather than varying in the text.
- Expand every acronym at first mention in the target text, even when the source already abbreviates it
  (OSPO, PMF, OPC, SIG). The source's own English glosses — 一人公司（OPC, One-Person Company）,
  SIG（Special Interest Group）— are kept as glosses, rephrased into English prose.
- Chinese company and product names use the company's own English name (智谱 → Zhipu AI,
  阶跃星辰 → StepFun, 书生系列 → Intern series). Never invent a pinyin name for an entity that has one;
  where no official English name is known, transliterate in pinyin and list it in the review reply.
  Project, repository, platform and license names stay verbatim (Dify, Qwen, ModelScope, Apache 2.0, MIT).
- 通义千问 and 千问 are the same thing → Qwen everywhere. Watch for other source-internal variants
  (Cherry studio / cherry-studio) and normalise to one spelling.

## Idiom and calque traps

Chinese policy idiom is the main quality risk. Do not translate image-by-image:

| Source | Do not write | Write |
|---|---|---|
| 抓手 | grip | lever, key mechanism |
| 卡点 / 瓶颈 | stuck point | bottleneck, constraint |
| 落地 | landing | deployment, adoption, implementation (pick by context) |
| 沉淀 (能力/资产) | precipitate | accumulate, build up, retain |
| 拉通 | pull through | connect, align, integrate |
| 高地 | highland | hub |
| 策源地 | source-ground | innovation source |
| 招商 / 招商引资 | attract business | investment promotion |
| 真金白银 | real gold and silver | concrete financial support |
| 拎包入驻 | carry-bag move-in | move-in ready |
| 弯道超车 | overtaking on the bend | leapfrog |
| 全托底 | fully bottomed | full backstop — "you bring the ideas, we handle the rest" |
| 我负责阳光雨露，你负责茁壮成长 | sunshine and rain | the government provides the conditions, firms do the growing |
| 一路一带-style 排比 | keep the parallelism | keep 2–3 short clauses, vary the verb, do not clone the syntax |

- 赋能 → empower only when it carries a real claim; when it is filler, use enable/support.
- Metaphors the source marks as its own (生态雨林, 共创智库, 智力外挂) keep the metaphor, in plain English
  ("ecosystem rainforest" → the open source ecosystem as soil and rainforest is fine; avoid inventing new ones).

## Numbers, dates, units

- Never keep 万 / 亿: 4500亿元 → RMB 450 billion; 1.7亿 → 170 million; 7万+Stars → 70,000+ GitHub stars;
  500万人 → 5 million people. Keep the source's precision and its hedges (超过/约 → over / around).
- Currency: 元 → RMB (write "RMB 450 billion"); 亿元 in tables may be abbreviated to RMB bn only if the
  table is narrow — otherwise spell it out.
- Percentages, ratios, index values (1:1.77, OpenRank 1600) keep their digits exactly.
- Dates: 2026年3月 → March 2026; 2025年1-8月 → January–August 2025; 二O二六年三月 → March 2026.
- Units and areas: ㎡ → m², 100万㎡ → 1 million m².
- Ranges written with --- in the source (2018---2020) become en dashes (2018–2020).
- Keep the source's own numbers wrong if they are wrong, and list the suspected error in the review reply.

## Names, organisations, documents

- Personal names: pinyin, family name last, no comma (徐旭初 → Xu Xuchu).
- Institutions: official English name where one exists (State Council, MIIT, CAICT, OpenAtom Foundation,
  Shanghai AI Laboratory); otherwise translate descriptively and give the pinyin in parentheses at first mention.
- Policy and document titles: use the official English title if the issuing body publishes one; otherwise
  translate the title and give the Chinese original in parentheses at first mention. Italicise titles
  (《关于深入实施"人工智能+"行动的意见》 → *Opinions on Deeply Implementing the "AI Plus" Initiative*),
  and never leave a bare 《…》 or a pinyin title.
- 政府工作报告 → the Government Work Report. 习近平总书记 → President Xi Jinping; quoted remarks
  use the official Xinhua English translation when one exists (check, do not improvise).
- "AI+" programme names keep the plus sign: "AI+ Manufacturing", "AI+ Government", "AI+ Consumption".

## Quotation marks and the source's emphasis

- The source wraps its own key concepts in curly double quotes ("项目集合", "生态思维", "应用牵引"). These are
  the author's scare quotes: keep them as English double quotes, do not delete them and do not turn them
  into italics.
- Bold is used structurally in the source (topic sentences, the four ecosystem models, term definitions).
  Preserve bold spans one-to-one. Never add bold of your own.
- Quote marks in the source are typographic Chinese quotes; convert to English curly quotes with proper nesting.

## Structure and formatting

- Headings: translate all of them, sentence case, keep the numbering exactly (3.3.2.1, 4.5, 5.6). Acronyms
  keep their case inside headings (AI, OPC, SIG).
- Enumerations: 一是/二是/三是 and 其一/其二/其三 become "First, … Second, … Third, …" inline in the same
  paragraph, and 首先/其次/最后 become "First / Second / Finally". Do not convert them into bullet lists.
- Footnote markers `[1]`–`[59]` are preserved verbatim: same markers, same positions, same order, same count.
  Never renumber, merge or reorder citations, even where the source cites the same number twice or looks
  miscited (e.g. a Shenzhen figure carrying a reference that points elsewhere) — list those in the review reply.
- The reference list keeps its `[n]` prefix and order. Translate Chinese titles and add the Chinese original in
  parentheses; keep URLs byte-identical, keep `[在线]` as `[Online]` and the 见于 dates as "accessed: <date>".
  Leave the leading note (\*注：…) translated but otherwise unchanged.
- Tables: keep row and column order, keep bold header cells, translate cell text only. Do not merge, split or
  re-sort rows, and do not "fix" a table whose headers do not match its content.
- Figures: 图 N → Figure N, 表 N → Table N, both in captions and in cross-references in the text.
  Image links keep their path unchanged; the alt text is translated (`![图 1：…](./media/image1.png)` →
  `![Figure 1: …](./media/image1.png)`). Keep the pandoc `{width=... height=...}` attributes.
- Case-study boxes: the leading 案例： inside a table cell becomes "Case Study: " and keeps the bold/plain
  formatting of the source. Do not restructure the box into a heading or a nested list.
- Preserve the source's paragraph breadths: same number of paragraphs, same order, no summarising, no
  added transitions, no translator's notes anywhere in the file.

## Known source defects (translate as-is, report, do not silently fix)

- Duplicate and mismatched footnote references, and one 《…》 title whose brackets are misplaced.
- Duplicated clauses (e.g. 维护了30+产业链上下游… appears twice in the OpenLoong box) — translate the
  duplicated text as it stands or collapse it only if you flag it.
- 深圳 para cites [24] where [33] is meant; 上海 OPC citation reuses [31].
- Typos in the source (GtiHub, 国AI开源, 完备治理) are not reproduced; render the intended meaning.

## Workflow expectations

- Long file: read it in segments by heading, translate segment by segment, write the complete English
  file once at the end (`中国人工智能开源生态蓝皮书.en.md`). Never stop after the first segment.
- Keep a running list of recurring source terms that are not in the glossary with the single rendering
  chosen for each; that list goes into the glossary-suggestions file, not into the prose.
