# English Translation Style Guide 英文翻译风格指南

> Source: issue #12 (bilingual proposal), cleaned for structure. Version and commit: see [Version control](#version-control-版本控制).
> The English text is normative. The Chinese text is a parallel reading aid.

**Genre:** A strategy-oriented Blue Book on national policy and industry development, combining policy analysis with case studies, tables, and footnotes. It is intended for international policy analysts, open source practitioners, and industry professionals.

**文体类型：** 一份围绕国家政策与产业发展展开、具有战略导向的蓝皮书，兼具政策分析、案例研究、表格和脚注。目标读者包括国际政策分析人士、开源实践者以及产业界专业人士。

## Audience and voice 目标读者与行文语气

- **Audience:** The intended audience consists of international readers who are familiar with open source and AI but may not be familiar with China-specific policy terminology, institutions, or domestic platforms. China-specific references must be explained clearly enough to be understood from the text without requiring the reader to consult a separate glossary.
  **目标读者：** 本书面向熟悉开源和人工智能，但未必熟悉中国特定政策术语、机构和本土平台的国际读者。涉及中国特定背景的内容，应在正文中解释得足够清楚，使读者无须另行查阅术语表也能理解。

- **Voice and tense:** Use a formal, neutral, and predominantly third-person voice. Preserve the first-person plural where the authors explicitly describe the report’s purpose, scope, methodology, or institutional position. Use the present tense for current conditions, general statements, and arguments; the past tense for completed historical events; and the present perfect where a development began in the past and remains relevant to the present.
  **语气与时态：** 全文应采用正式、中性且以第三人称为主的行文语气。当作者明确说明本报告的目的、范围、研究方法或机构立场时，可以保留第一人称复数。描述当前状况、一般性陈述和论点时使用现在时；描述已经完成的历史事件时使用过去时；描述始于过去并且至今仍有现实意义的发展时，可以使用现在完成时。

- **Argument and policy rhetoric:** Preserve the source’s substantive arguments, causal claims, qualifications, and criticism, including criticism of Chinese institutions and other actors. Render slogan-like or formulaic policy language as precise, neutral English where possible, but do not omit substantive content or alter the author’s position. Preserve the wording of official slogans or directly quoted expressions when the wording itself is relevant.
  **论点与政策修辞：** 应保留原文中的实质性论点、因果判断、限定条件和批评，包括对中国机构及其他参与主体的批评。在条件允许时，应将口号式或程式化的政策语言转化为准确、中性的英文，但不得因此删减实质内容或改变作者立场。如果官方口号或直接引语本身具有分析意义，则应保留其措辞。

- **Promotional language and punctuation:** Do not introduce promotional adjectives, unsupported superlatives, exclamation marks, or other marketing language that is not present in the source. Where the source itself uses promotional or slogan-like language, retain the underlying substantive claim while removing only empty rhetorical padding. Do not neutralize language whose evaluative force is integral to the author’s argument.
  **宣传性语言与标点：** 不得增加原文没有的宣传性形容词、缺乏依据的最高级、感叹号或其他营销语言。如果原文本身使用宣传性或口号式表达，应保留其中的实质性论断，只删除不承载实际意义的修辞性包装。如果某种评价性语气是作者论证不可分割的一部分，则不得将其刻意中性化。

- **Strength of claims:** Do not soften or strengthen the source’s claims. Preserve its modality, degree of certainty, evidentiary strength, and qualifying language. For example, 面临若干关键瓶颈 should be translated as `faces several key bottlenecks`, not the weaker `faces some challenges` or the stronger `faces severe structural barriers`.
  **论断强度：** 不得弱化或强化原文论断。应保留原文的情态、确定程度、证据强度和限定性表达。例如，“面临若干关键瓶颈”应译为 faces several key bottlenecks，不能弱化为 faces some challenges，也不能强化为 faces severe structural barriers。

## Terminology 术语

- **Status of the glossary:** The glossary (`glossary.csv`, column `status`) is the project’s primary terminology reference. Only entries marked `approved` are binding across the book. Entries marked `preferred` should be used by default but may be adjusted where the context requires. Entries marked `context-dependent` should be translated according to their meaning and collocation in the relevant passage. Entries marked `verification required` must not be treated as final until an official name or authoritative source has been confirmed.
  **术语表的效力：** Glossary（`glossary.csv` 的 `status` 列）是本项目首要的术语参考。只有标记为 `approved`（已批准）的词条，才对全书具有约束力。标记为 `preferred`（推荐使用）的词条原则上应优先采用，但在语境确有需要时可以调整。标记为 `context-dependent`（取决于语境）的词条，应根据其在具体段落中的含义和搭配进行翻译。标记为 `verification required`（需要核实）的词条，在官方名称或权威来源得到确认之前，不得视为最终译法。

- **Consistency and context:** Apply an approved rendering consistently whenever the same term is used in the same sense. Do not substitute synonyms merely for stylistic variety. However, do not force a single English rendering across distinct meanings or contexts of the same Chinese expression. Record recurring context-dependent choices in the glossary or glossary-suggestions file.
  **一致性与语境：** 当同一个术语表达相同义项时，应始终采用已经批准的译法，不得仅仅为了追求措辞变化而随意替换同义词。但是，如果同一个中文表达在不同语境中具有不同含义，也不得强迫其一律对应同一个英文译法。反复出现的语境化译法应记录在 glossary 或 glossary-suggestions 文件中。

- **Chinese policy terminology:** Use an official published English rendering where one exists. Otherwise, use the project’s approved or preferred translation. Do not assume that policy terms such as 自主可控, 卡脖子, 耐心资本, and 规上企业 have a single universally settled English equivalent. Where the appropriate rendering remains uncertain or context-dependent, record the issue in the review log rather than introducing an undocumented alternative.
  **中国政策术语：** 如果某个政策术语已有正式发布的官方英文译法，应采用该译法；否则，应采用项目已经批准或推荐的译法。不得假设“自主可控”“卡脖子”“耐心资本”和“规上企业”等政策术语都存在唯一且得到普遍认可的英文对应词。如果合适的译法仍不确定或需要根据语境决定，应将问题记录在审校日志中，而不是自行采用没有记录的新译法。

- **Acronyms and source-supplied English glosses:** Expand unfamiliar acronyms at their first substantive mention in the main text, followed by the acronym in parentheses. Acronyms widely understood by the intended readership, such as AI and US, need not be expanded. Recast source-supplied English glosses into natural English order: 一人公司（OPC, One-Person Company） → `one-person company (OPC)`; SIG（Special Interest Group） → `special interest group (SIG)`. A use in a heading does not count as the first substantive mention. Redefine an unfamiliar acronym in a table, figure, caption, or case-study box when that element is intended to be read independently.
  **缩写及原文自带的英文释义：** 对目标读者可能不熟悉的缩写，应在正文中第一次实质性出现时写出全称，并在括号中注明缩写。对于 AI、US 等目标读者普遍熟悉的缩写，无须展开。原文自带的英文释义应按照自然的英文顺序重新组织，例如“一人公司（OPC, One-Person Company）”应写成 one-person company (OPC)；“SIG（Special Interest Group）”应写成 special interest group (SIG)。缩写仅在标题中出现，不视为第一次实质性出现。如果某个表格、图片、图注或案例框需要独立阅读，则应在必要时重新解释其中不常见的缩写。

- **Companies, products, projects, and platforms:** Use the entity’s verified official English name and official capitalization—for example, 智谱 → `Zhipu AI`, 阶跃星辰 → `StepFun`, and 通义千问 → `Qwen`. Do not invent an English name or pinyin form when an official English name already exists. Where no official English name can be verified, use Hanyu Pinyin or a clear descriptive translation, as appropriate to the type of entity, and provide sufficient identification at first mention. Record the proposed form and its verification status in the review log. Preserve exact repository identifiers, account names, and URLs where they are case-sensitive.
  **公司、产品、项目与平台名称：** 应采用相关主体经过核实的官方英文名称和官方大小写形式，例如“智谱”译为 `Zhipu AI`，“阶跃星辰”译为 `StepFun`，“通义千问”译为 `Qwen`。如果已经存在官方英文名称，不得自行创造其他英文名称或拼音形式。如果无法核实官方英文名称，则应根据相关主体的类型，酌情使用汉语拼音或清晰的描述性译名，并在第一次出现时提供足够的识别信息。建议名称及其核实状态应记录在审校日志中。对于区分大小写的 repository identifier、账户名称和网址，应保留其准确形式。

- **Licenses:** Use the official license name in running text, such as `Apache License 2.0` or `MIT License`. Use an SPDX identifier, such as `Apache-2.0` or `MIT`, only where a machine-readable identifier or compact tabular form is appropriate. Do not treat an informal label such as `Modified MIT` as a standardized license without verifying the specific license text.
  **许可证：** 正文中应使用许可证的官方名称，例如 `Apache License 2.0` 或 `MIT License`。只有在需要机器可读标识符或表格空间有限时，才使用 `Apache-2.0` 或 `MIT` 等 SPDX identifier。未经具体许可证文本核实，不得将 `Modified MIT` 等非正式标签视为标准化许可证名称。

- **Aliases and spelling variants:** Normalize inconsistent names and spellings only after confirming that they refer to the same entity and perform the same naming function. In this text, 通义千问 and 千问 refer to the same product family and should normally be rendered as `Qwen`. Use `Cherry Studio` for the product name, but preserve `cherry-studio` where it is the exact repository slug, package name, account name, or URL component. Record unresolved identity or naming questions in the review log.
  **别称与拼写变体：** 只有在确认不同名称或拼写确实指向同一个主体，并且承担相同命名功能之后，才能将其统一。在本书中，“通义千问”和“千问”指向同一个产品系列，通常应统一译为 `Qwen`。产品名称应写成 `Cherry Studio`；但当 `cherry-studio` 是准确的 repository slug、软件包名称、账户名称或网址组成部分时，应保留该形式。尚未解决的主体身份或命名问题应记录在审校日志中。

## Idiom and calque traps 习语与直译陷阱

Chinese policy idiom is the main quality risk. Do not translate image-by-image:

| Source | Do not write | Write |
| :---- | :---- | :---- |
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
- Metaphors the source marks as its own (生态雨林, 共创智库, 智力外挂) keep the metaphor, in plain English ("ecosystem rainforest" → the open source ecosystem as soil and rainforest is fine; avoid inventing new ones).

## Numbers, dates, units 数字、日期与计量单位

- **Chinese numerical units:** Convert Chinese large-number units such as 万 and 亿 into forms that are immediately intelligible to international readers. For example: 4500亿元 → `RMB 450 billion`; 1.7亿 → `170 million`; 7万+ Stars → `more than 70,000 GitHub stars` in running text or `70,000+ GitHub stars` in a compact table; and 500万人 → `5 million people`. Check all conversions carefully.
  **中文大数单位：** 将“万”和“亿”等中文大数单位转换为国际读者能够直接理解的表达。例如：4500亿元译为 `RMB 450 billion`；1.7亿译为 `170 million`；7万+ Stars 在正文中译为 `more than 70,000 GitHub stars`，在空间有限的表格中可以写成 `70,000+ GitHub stars`；500万人译为 `5 million people`。所有数值换算均须仔细核对。

- **Precision and qualification:** Preserve the source’s numerical value, level of precision, and qualifying language. Do not introduce additional decimal places, unnecessary rounding, or greater certainty than the source provides. Translate 超过 as `more than` or `over`, and 约 as `approximately`, `about`, or `around`, according to context. Handle suspected numerical errors through the source-error procedure rather than correcting them silently.
  **精度与限定表达：** 保留原文的数值、精度和限定程度。不得增加原文没有的小数位数，不得进行不必要的四舍五入，也不得使表述显得比原文更加确定。“超过”可根据语境译为 more than 或 over；“约”可根据语境译为 approximately、about 或 around。对于疑似错误的数字，应按照原文错误处理程序解决，不得擅自修正。

- **Currency:** Express amounts in Chinese yuan using `RMB` before the figure—for example, `RMB 450 billion`. Do not convert RMB amounts into another currency unless the source provides the conversion or the authors approve it. In running text, spell out `million` and `billion`. In a space-constrained table, abbreviated units such as `RMB mn` or `RMB bn` may be used only if the abbreviation is defined clearly in the column heading or a table note. Where practical, use a heading such as `Amount (RMB billion)` and place only the numerical values in the cells.
  **货币：** 人民币金额统一在数字前使用 RMB，例如 RMB 450 billion。除非原文已经提供货币换算，或作者批准进行换算，否则不得擅自将人民币金额换算成其他货币。正文中应完整写出 million 和 billion。在空间有限的表格中，只有在列标题或表下注释已经明确定义的情况下，才能使用 RMB mn 或 RMB bn 等缩写。在条件允许时，建议将表头写成 Amount (RMB billion)，单元格中只填写数值。

- **Percentages, ratios, and index values:** Preserve the source value and level of precision while applying standard English numerical formatting. Use commas as thousands separators where appropriate: OpenRank 1600 → `an OpenRank score of 1,600`. Retain ratios in their original mathematical form, such as `1:1.77`, unless the surrounding sentence requires an explanatory reformulation. Write percentages without a space before the percent sign, for example, `70%`.
  **百分比、比率和指数值：** 保留原文数值及其精度，同时按照英文数字格式进行规范处理。适当使用千位分隔符，例如 OpenRank 1600 可写为 an OpenRank score of 1,600。比率原则上保留原有的数学形式，例如 1:1.77；只有在上下文需要解释时才改写。百分号与前面的数字之间不留空格，例如 70%。

- **Dates:** Use American English date conventions. Translate 2026年3月 as `March 2026`; 2025年8月27日 as `August 27, 2025`; 2025年1–8月 as `January–August 2025`; and 二〇二六年三月 as `March 2026`. Preserve the source’s level of precision: do not add a day or month that the source does not provide.
  **日期：** 采用美式英语日期格式。2026年3月译为 March 2026；2025年8月27日译为 August 27, 2025；2025年1—8月译为 January–August 2025；二〇二六年三月译为 March 2026。应保留原文的时间精度；如果原文没有提供具体月份或日期，不得自行补充。

- **Units and areas:** Use standard SI symbols and formatting. Translate ㎡ as `m²` and 100万㎡ as `1 million m²`. Insert a space between the numerical value and the unit symbol—for example, `100 m²`, `5 km`, and `20 MW`—except where standard convention requires otherwise, as with percentages. Unit symbols do not take plural endings or periods.
  **计量单位与面积：** 使用标准国际单位制符号和格式。“㎡”译为 m²，100万㎡译为 1 million m²。数字与单位符号之间应留一个空格，例如 100 m²、5 km 和 20 MW；百分比等另有通行规范的情况除外。单位符号不使用复数形式，也不加句点。

- **Ranges:** Replace hyphens or repeated hyphens used as range markers with an en dash, without surrounding spaces: 2018---2020 → `2018–2020`. When a range is introduced by `from`, use `to` rather than an en dash: `from 2018 to 2020`, not `from 2018–2020`.
  **范围：** 原文使用连字符或多个连字符表示范围时，应统一改用前后不留空格的 en dash，例如 2018---2020 改为 2018–2020。如果范围前使用 from，则应与 to 搭配，不使用 en dash，即写成 from 2018 to 2020，而不是 from 2018–2020。

## Names, organizations, documents 人名、机构与文件名称

- **Personal names:** For Chinese names written in Hanyu Pinyin, preserve Chinese name order, with the family name first, and write the family name in uppercase without a comma (徐旭初 → `XU Xuchu`; 习近平 → `XI Jinping`). Do not reverse pinyin names into Western name order. Where an individual has an established English name or personally preferred English form, retain that established form while writing the family name in uppercase where it can be identified reliably (Jack Ma → `Jack MA`). Apply this convention consistently in the main text, captions, tables, case studies, and contributor lists.
  **人名：** 对于使用汉语拼音书写的中国人姓名，应保留中国姓名顺序，即姓在前、名在后，并将姓氏的拼音全部大写，中间不加逗号，例如徐旭初译为 `XU Xuchu`，习近平译为 `XI Jinping`。不得将拼音姓名倒置为西方姓名顺序。如果相关个人已有固定使用或本人偏好的英文姓名形式，则保留其既有英文姓名顺序；在能够可靠判断姓氏的情况下，将姓氏全部大写，例如 Jack Ma 写作 `Jack MA`。这一规范应统一应用于正文、图注、表格、案例和编写人员名单。

- **Organizations and institutions:** Use the organization’s official English name where one exists. At first mention, use the full official name followed by its established abbreviation in parentheses, where applicable—for example, the Ministry of Industry and Information Technology (MIIT), the China Academy of Information and Communications Technology (CAICT), the OpenAtom Foundation, and the Shanghai Artificial Intelligence Laboratory. An established short form may be used subsequently. Where no official English name exists, provide a clear descriptive translation followed by the Chinese original in parentheses at first mention. Add pinyin only when it is useful for identifying a proper name or brand; do not use pinyin as a substitute for an intelligible translation.
  **组织与机构：** 如果相关组织存在官方英文名称，应采用其官方名称。首次出现时，应使用完整的官方英文名称，并在适用的情况下于括号中注明其通行缩写，例如 Ministry of Industry and Information Technology (MIIT)、China Academy of Information and Communications Technology (CAICT)、OpenAtom Foundation 和 Shanghai Artificial Intelligence Laboratory。后续可以使用已经确立的简称。如果不存在官方英文名称，首次出现时应提供清晰、可理解的描述性英文译名，并在括号中附上中文原名。只有当拼音有助于识别专有名称或品牌时才予以添加；不得以拼音代替国际读者可以理解的翻译。

- **Policy and document titles:** Use the official English title published by the issuing body where one exists, and record the verification source in the review log. Otherwise, provide a clear English translation followed by the Chinese original in parentheses at first mention. Italicize the titles of standalone reports and policy documents consistently. For example: *Opinions on Deepening the Implementation of the “AI Plus” Initiative* (《关于深入实施“人工智能+”行动的意见》). Treat an editor-produced translation as a working title unless and until an official English title has been verified. Do not leave a bare Chinese title or an unexplained pinyin title in the English text.
  **政策与文件标题：** 如果发布机构公布了官方英文标题，应采用该标题，并在审校日志中记录核实来源。如果不存在官方英文标题，首次出现时应提供清晰的英文译名，并在括号中附上中文原题。独立报告和政策文件的标题应统一使用斜体。例如：*Opinions on Deepening the Implementation of the “AI Plus” Initiative*（《关于深入实施“人工智能+”行动的意见》）。编辑或译者拟定的英文标题在官方英文标题得到核实之前，应视为暂定译名。英文正文中不得只保留没有翻译的中文标题，也不得只提供未经解释的拼音标题。

- **Government work reports:** Use the Government Work Report when referring to the annual national report. For a provincial, municipal, or other local report, identify the relevant jurisdiction—for example, the Shanghai Municipal Government Work Report.
  **政府工作报告：** 指全国年度政府工作报告时，使用 the Government Work Report。如果指省级、市级或其他地方政府工作报告，应注明相应行政区域，例如 the Shanghai Municipal Government Work Report。

- **Official titles of individuals:** Preserve the office or capacity specified in the source. Translate 习近平总书记 as XI Jinping, general secretary of the Communist Party of China Central Committee at first mention, or as General Secretary XI Jinping where the institutional context is already clear. Translate 国家主席习近平 as President XI Jinping. Do not replace one official title with another merely because the alternative may be more familiar to international readers.
  **个人的正式职务：** 应保留原文所指明的职务或身份。首次出现“习近平总书记”时，可译为 XI Jinping, general secretary of the Communist Party of China Central Committee；如果上下文已经明确相关机构，也可以使用 General Secretary XI Jinping。“国家主席习近平”应译为 President XI Jinping。不得仅仅因为另一个职务名称可能更为国际读者熟悉，就用其替换原文中的正式职务。

- **Official quotations:** Use an authoritative published English version of an official quotation where one is available. Give priority to the issuing institution’s English-language publication, followed by an official central-government source and then an official news agency such as Xinhua. Record the source used. Where no official English version exists, translate the quotation faithfully and record that the English wording is translator-produced; do not present an unverified translation as official.
  **官方引语：** 如果某段官方引语已有权威发布的英文版本，应采用该版本。检索来源的优先顺序依次为：发布机构自身的英文出版物、中央政府官方英文来源，以及新华社等官方通讯社。应记录所采用的来源。如果不存在官方英文版本，应忠实翻译引语，并注明该英文表述由译者翻译；不得将未经核实的译文当作官方译文。

- **“AI Plus” and AI+ names:** Follow the verified official English form of each initiative or program. In general prose, use the “AI Plus” initiative. Retain the plus sign in forms such as AI+ only when it is part of a verified official program, project, or brand name. Do not invent English labels such as AI+ Government or AI+ Consumption without an authoritative source.
  **“AI Plus”与 AI+ 名称：** 每项行动、计划或项目均应采用经过核实的官方英文形式。在一般正文中，使用 the “AI Plus” initiative。只有当 AI+ 确实属于经过核实的正式计划、项目或品牌名称时，才保留加号。没有权威来源时，不得自行创造 AI+ Government 或 AI+ Consumption 等英文名称。

## Quotation marks and source emphasis 引号与原文强调方式

- Chinese quotation marks may indicate direct quotations, coined or defined terms, conceptual labels, emphasis, or authorial distance. Determine their function from the context; do not automatically treat all quoted key concepts as scare quotes.
  中文引号可能表示直接引语、作者新造或明确定义的术语、概念标签、强调，或者作者有意表达的疏离态度。应根据具体语境判断引号的功能，不得自动将所有加引号的关键概念都视为带有质疑或讽刺意味的“警示引号”（scare quotes）。

- For a coined, defined, or explicitly introduced term, retain English double quotation marks at first mention where they help signal its status as a term. Subsequent mentions may appear without quotation marks unless the repeated quotation marks convey a substantive rhetorical function, such as contrast, skepticism, or authorial distance. Preserve genuine scare quotes where they are necessary to retain the author’s stance.
  对于作者新造、明确定义或正式引入的术语，如果英文双引号有助于表明其术语性质，应在第一次出现时保留英文双引号。后续出现时可以不再使用引号，除非原文重复使用引号具有实质性的修辞功能，例如表示对比、质疑或作者刻意保持距离。对于确实表达作者立场的警示引号，应予以保留。

- For direct quotations, use an authoritative published English translation where one is available. Otherwise, translate the quotation faithfully and retain its status as a direct quotation. Do not silently paraphrase, shorten, or merge quoted material.
  对于直接引语，如果存在权威的正式英文译文，应优先采用。不存在正式译文时，应忠实翻译引语，并保留其作为直接引语的形式。不得在不作说明的情况下擅自改写、缩短或合并引语内容。

- Preserve bold formatting when it performs a clear structural or semantic function, such as identifying topic sentences, ecosystem-model labels, or defined terms. Do not mechanically reproduce accidental bolding, isolated bold punctuation, or Markdown conversion artifacts. Do not introduce new bold emphasis unless it is required to apply an established formatting pattern consistently.
  当粗体具有明确的结构或语义功能时，应予以保留，例如用于标示主题句、生态模式名称或定义术语。但不得机械复制误加粗、单独加粗的标点符号或 Markdown 格式转换过程中产生的异常格式。除非为了统一执行已经确立的格式规则，否则不得自行增加原文没有的粗体强调。

- Convert Chinese typographic quotation marks to English curly quotation marks. Use double quotation marks for the outer quotation and single quotation marks for a quotation within a quotation. Follow American English punctuation conventions. Chinese book-title marks (《…》) are not quotation marks and must be handled according to the rules for document and publication titles.
  中文排版引号应转换为英文弯引号。外层引语使用英文双引号，嵌套在引语内部的引语使用英文单引号。标点位置遵循美式英语规范。中文书名号（《……》）不属于普通引号，应按照文件和出版物标题的相关规则处理。

## Structure and formatting 结构与格式

- **Headings:** Translate all headings and use sentence case, while preserving their numbering and hierarchical level exactly (for example, 3.3.2.1, 4.5, and 5.6). Acronyms retain their established capitalization within headings (AI, OPC, SIG). Proper names retain their official styling.
  **标题：** 翻译所有标题，并统一采用 sentence case，即除专有名称和缩写外，通常只将标题首词的首字母大写。标题的编号和层级必须准确保留，例如 3.3.2.1、4.5 和 5.6。标题中的缩写应保留其既定的大写形式，例如 AI、OPC 和 SIG。专有名称则保留其官方书写形式。

- **Enumerations:** Preserve the sequence, hierarchy, and rhetorical emphasis of enumerations in the source. Render 一是／二是／三是 and 其一／其二／其三 as “First, … Second, … Third, …” where this is natural in English; render 首先／其次／最后 as “First, … Second, … Finally, …” where appropriate. Do not automatically convert inline enumerations into lists. A numbered or bulleted list may be used only when the source already functions as a list, the change materially improves readability, and no content or hierarchy is altered.
  **列举结构：** 保留原文列举内容的先后顺序、层级关系和修辞重点。在英语表达自然的情况下，将“一是／二是／三是”和“其一／其二／其三”译为“First, … Second, … Third, …”；将“首先／其次／最后”酌情译为“First, … Second, … Finally, …”。不得自动将段落内的列举结构转换成项目列表。只有当原文在功能上已经构成列表、改用编号或项目符号能够显著提高可读性，而且不会改变任何内容或层级时，才可以使用编号或项目符号列表。

- **Footnote and citation markers:** Preserve the same markers, order, and total count unless a correction has been confirmed through the source-error procedure. Keep each marker attached to the same proposition or claim as in the source, but allow its precise position within the sentence to shift where required by English syntax. Do not silently renumber, merge, delete, or reorder citations. Record suspected duplicate, misplaced, or incorrect citations in the review log and mark them for author verification.
  **脚注和引文标记：** 除非有关修正已经通过原文错误处理程序得到确认，否则应保留相同的标记、排列顺序和总数。每个标记必须继续对应原文中的同一命题或论断；但如果英文句法有此需要，可以调整标记在句子内部的具体位置。不得擅自重新编号、合并、删除或调整引文顺序。对于疑似重复、错置或不正确的引文，应记录在审校日志中，并标记为需要作者核实。

- **Reference list:** Preserve the [n] prefixes and the order of entries. Use an official English title where one exists; otherwise, translate the Chinese title and include the Chinese original in parentheses. Preserve URL destinations and do not replace or correct links without verification. Render [在线] as [Online] and 见于 dates as accessed Month Day, Year, following American English date conventions. Translate the leading note (\*注：…) while preserving its function and position.
  **参考文献表：** 保留每条文献前的 [n] 标记及其排列顺序。如果文件或文献存在官方英文标题，应采用官方标题；如果没有，则翻译中文标题，并在括号中附上中文原题。保持网址所指向的链接目标不变；未经核实，不得擅自替换或修正链接。将 [在线] 译为 [Online]，并按照相应的美式英语日期格式，将“见于”日期写为 accessed Month Day, Year。开头的说明文字（\*注：……）应予以翻译，同时保留其原有功能和位置。

- **Tables:** Preserve the order of rows and columns, the underlying data, and meaningful header formatting. Translate the text within cells without merging, splitting, or re-sorting rows unless the authors approve the change. If a table header does not match its content, do not correct it silently; record the issue in the review log and handle it through the source-error procedure.
  **表格：** 保留原表格的行列顺序、基础数据和具有实际意义的表头格式。翻译单元格中的文字；未经作者批准，不得合并、拆分或重新排列各行。如果表头与表格内容不匹配，不得擅自修改；应将问题记录在审校日志中，并按照原文错误处理程序解决。

- **Figures and tables:** Render 图 N as Figure N and 表 N as Table N in captions and all cross-references. Translate existing alt text while keeping image paths unchanged. Preserve Pandoc attributes such as `{width=... height=...}`. Confirm that every figure and table reference in the text corresponds to the correct caption and number.
  **图片与表格：** 在图片和表格标题以及正文中的所有交叉引用中，将“图 N”译为 Figure N，将“表 N”译为 Table N。翻译原有的替代文本，但保持图片路径不变。保留 `{width=... height=...}` 等 Pandoc 属性。检查正文中每一处图表引用，确保其与正确的图表标题和编号相对应。

- **Case-study boxes:** Translate the leading 案例： within a table cell as Case Study: and preserve the box’s structural function and meaningful formatting. Do not convert a case-study box into a heading, ordinary paragraph, or nested list without author approval.
  **案例框：** 将表格单元格开头的“案例：”译为 Case Study:，并保留案例框的结构功能和具有实际意义的格式。未经作者批准，不得将案例框改为标题、普通段落或嵌套列表。

- **Paragraph structure:** Preserve the order, substantive content, evidence, and argumentative relationships of the source. Sentence boundaries and paragraph breaks may be adjusted where necessary for idiomatic English and readability, provided that no claim, qualification, example, or emphasis is added or omitted. Do not summarize the source or add substantive transitions that are not supported by it. Explanatory first-mention glosses required by the glossary or style guide may be included; other translator’s notes and editorial explanations belong in the review log unless the authors approve their inclusion in the text.
  **段落结构：** 保留原文的内容顺序、实质内容、论据和论证关系。为了使英文表达自然、便于阅读，可以在必要时调整句子边界和段落划分，但不得增加或遗漏任何论断、限定条件、例子或强调。不得概括原文，也不得添加原文没有依据的实质性过渡内容。Glossary 或 style guide 要求在术语首次出现时加入的解释性说明可以保留；其他译者注和编辑说明应记录在审校日志中，除非作者批准将其纳入正文。

- **Markdown integrity:** Preserve valid Markdown syntax, code spans, link destinations, relative file paths, image paths, and Pandoc attributes. Preview or render the completed file to verify that headings, tables, lists, links, images, footnotes, and other structural elements display correctly.
  **Markdown 完整性：** 保留有效的 Markdown 语法、行内代码、链接目标、相对文件路径、图片路径和 Pandoc 属性。文件完成后，应进行预览或渲染，检查标题、表格、列表、链接、图片、脚注以及其他结构元素能否正确显示。

## Source errors and editorial queries 原文错误与编辑待确认事项

Do not silently alter substantive facts, figures, quotations, citations, or the structure of the source text. All suspected source errors must be recorded in the review log and handled according to the procedures below.

不得擅自修改涉及实质内容的事实、数字、引语、文献引用或原文结构。所有疑似原文错误均须记录在审校日志中，并按照以下程序处理。

- **Obvious typographical or formatting errors:** Clear typographical and formatting errors, such as *GtiHub*, *国AI开源*, or misplaced punctuation and brackets, may be corrected in the English translation. Each correction must nevertheless be recorded in the review log.
  **明显的拼写或格式错误：** 对于明确无疑的拼写和格式错误，例如 GtiHub、国AI开源，以及明显错置的标点符号或括号，可以在英文译文中直接修正。但每一项修正仍须记录在审校日志中。

- **Suspected factual, numerical, quotation, or citation errors:** Do not correct these without author confirmation. Mark each case as `author verification required` in the review log. Pending confirmation, preserve the source information in the working translation, but do not treat the passage as final or ready for publication.
  **疑似事实、数字、引语或文献引用错误：** 未经作者确认，不得擅自修改。每一处此类问题均须在审校日志中标记为 `author verification required`（需要作者核实）。在获得确认之前，应在工作译稿中暂时保留原文信息，但不得将相关段落视为已经定稿或可以正式发布。

- **Duplicated or structurally inconsistent content:** Duplicated passages, mismatched table headers, misplaced references, and similar structural problems must not be deleted, collapsed, rearranged, or otherwise corrected without author approval. Pending confirmation, preserve the source structure and record the problem in the review log.
  **重复或结构不一致的内容：** 对于重复段落、表头与内容不匹配、引用位置错误，以及其他类似的结构问题，未经作者批准，不得擅自删除、合并、重新排列或以其他方式修正。在获得确认之前，应保留原文结构，并将有关问题记录在审校日志中。

- **Confirmed corrections:** Once an error has been confirmed, correct both the Chinese source and the English translation wherever possible. If the Chinese source cannot be updated, record the author-approved difference between the two versions in the review log.
  **已经确认的修正：** 一旦错误得到确认，应尽可能同时修改中文原稿和英文译文。如果中文原稿无法更新，则须在审校日志中记录经过作者批准的中英文版本差异。

## Known source issues requiring review 需要审阅的已知原文问题

- The source contains duplicate or mismatched footnote references and one document title with misplaced brackets. These cases require author verification.
  原文存在重复或不匹配的脚注引用，另有一处文件标题的书名号位置错误。这些情况均需要作者核实。

- The OpenLoong case-study box repeats the clause beginning with “维护了30+产业链上下游……”. Preserve the duplication pending author confirmation; do not collapse it solely on the basis that it has been flagged.
  OpenLoong 案例框中重复出现了以“维护了30+产业链上下游……”开头的语句。在作者确认之前，应保留该重复内容；不能仅仅因为该问题已被发现或标记，就直接将其合并或删除。

- The Shenzhen paragraph appears to cite [24] where [33] may have been intended, while the Shanghai OPC discussion reuses [31]. Mark both cases as `author verification required`.
  深圳部分似乎引用了 [24]，但原本可能应为 [33]；上海 OPC 部分则重复使用了 [31]。这两处均应标记为 `author verification required`（需要作者核实）。

- Obvious typographical errors, including *GtiHub*, *国AI开源*, and *完备治理*, should be rendered according to their intended meaning in the English translation and recorded in the review log.
  对于原文中明显的拼写或排版错误，包括 *GtiHub*、*国AI开源* 和 *完备治理*，应在英文译文中按照作者原意进行处理，并将有关修改记录在审校日志中。

## Workflow expectations 工作流程要求

- Translate long files in manageable sections organized by heading. Save completed sections incrementally in a version-controlled working file or through separate commits, and integrate them into the final English file (中国人工智能开源生态蓝皮书.en.md). Clearly label any partial translation as a work in progress; it must not be presented as a completed deliverable.
  长篇文件应按照标题结构划分为便于管理的若干部分，逐部分进行翻译。已经完成的部分应及时保存到具有版本记录的工作文件中，或通过独立的 commit 分阶段提交，随后整合进最终英文文件（中国人工智能开源生态蓝皮书.en.md）。任何尚未完成的部分译文都必须明确标记为工作稿，不得作为完整交付成果提交。

- At the beginning of each section, consult the current approved versions of the style guide and glossary. The translation record must identify the versions of the Chinese source, style guide, and glossary used.
  开始翻译每个部分之前，应查阅当前已经批准的 style guide 和 glossary 版本。翻译记录必须注明所依据的中文原稿、style guide 和 glossary 的具体版本。

- Maintain a running list of recurring source terms that are not yet included in the glossary. For each term, record the source term, proposed English rendering, relevant meaning or context, rationale, verification source, and approval status in the glossary-suggestions file. Do not force a single English rendering across distinct meanings of the same Chinese term. Once a proposed rendering has been approved, apply it consistently wherever the same meaning recurs and add it to the main glossary.
  持续记录原文中反复出现但尚未收入 glossary 的术语。对于每个术语，应在 glossary-suggestions 文件中记录中文原词、建议英文译法、相关义项或语境、修改理由、核实来源和批准状态。不得强迫同一个中文词在不同义项下使用同一个英文译法。建议译法获得批准后，应在相同义项再次出现时保持一致，并将其收入正式 glossary。

- Record unresolved terminology, factual, citation, and source-text issues in the review log rather than inserting translator’s notes into the English prose.
  尚未解决的术语、事实、引文和原文问题应记录在 review log 中，而不应以译者注的形式插入英文正文。

- Before final delivery, conduct a completeness and consistency check. Confirm that all headings, tables, figures, captions, case-study boxes, citations, footnotes, and reference-list entries have been translated and retained; verify terminology against the approved glossary; check internal cross-references and links; and ensure that every unresolved issue is recorded in the review log.
  最终交付前，应进行完整性和一致性检查。确认所有标题、表格、图片、图注、案例框、引文、脚注和参考文献条目均已翻译并得到保留；按照已经批准的 glossary 检查术语；核对内部交叉引用和链接；并确认所有尚未解决的问题都已记录在 review log 中。

- The final deliverable must consist of one complete English file. It should not be marked as final until all sections have been integrated, the required checks have been completed, and any issues designated as blocking have been resolved.
  最终交付成果应为一份完整的英文文件。在所有部分完成整合、必要检查全部完成，并且被标记为阻断性问题的事项得到解决之前，不得将该文件标记为最终版本。

## Additional house rules 补充编辑规范

- **Language variety:** Use American English throughout the book. Apply American spelling consistently, including *organizations*, *italicize*, *normalize*, and *summarizing*. Do not mix American and British spelling within the text.
  **英语变体：** 全书统一采用美式英语，并始终使用美式拼写，例如 *organizations*、*italicize*、*normalize* 和 *summarizing*。同一文本中不得混用美式和英式拼写。

- **Use of “open source”:** Write *open source* as two unhyphenated, lowercase words, including when it functions as a modifier: *open source software*, *open source community*, and *open source AI ecosystem*. Capitalize it only when it forms part of an official proper name or document title.
  **“open source”的写法：** *open source* 统一写成两个不加连字符的小写单词，包括用作前置修饰语时，例如 *open source software*、*open source community* 和 *open source AI ecosystem*。只有当其属于正式专有名称或文件标题的一部分时才使用大写。

- **“Open source AI” and “open-weight”:** Do not treat *open source AI* and *open-weight* as interchangeable. Translate the source terminology faithfully, but flag any case in which a model described as open source appears to provide only open weights or otherwise may not satisfy the relevant open source criteria. Do not silently replace *open source* with *open-weight*. Use *open-weight* only when this description is supported by the source or approved by the authors after verification.
  **“open source AI”与“open-weight”：** 不得将 *open source AI* 和 *open-weight* 视为可以互换的概念。翻译时应忠实反映原文用语；但如果原文将某个仅公开权重，或可能不符合相关开源标准的模型称为“开源”，应将该问题记录在审校日志中。不得擅自将 *open source* 改为 *open-weight*。只有在原文有依据，或经核实并获得作者确认后，才使用 *open-weight*。

- **Review log:** Record unresolved translation, terminology, factual, citation, and source-text issues in a structured review log. Each entry should include: location, source text, current translation, proposed translation, rationale, verification source, and status. Use consistent status values, such as open, verification required, author decision required, approved, and resolved. Where applicable, the verification source should include a URL and access date.
  **审校日志：** 所有尚未解决的翻译、术语、事实、引文和原文问题，均应记录在结构化的审校日志中。每条记录应包含：位置、中文原文、当前译文、建议译文、修改理由、核实来源和处理状态。处理状态应使用统一选项，例如：待处理、需要核实、需要作者决定、已批准和已解决。如适用，核实来源应包含网址和访问日期。

### Version control 版本控制

- The style guide and glossary must each display a version number, last-updated date, and, where applicable, the relevant Git commit. Translation files and review logs must identify the versions of the source text, style guide, and glossary used. Do not cite a moving branch such as main as the sole version reference when a specific commit is available.
  Style guide 和 glossary 均须注明版本号、最后更新日期，并在适用时注明对应的 Git commit。译文文件和审校日志须记录其所依据的中文原稿、style guide 和 glossary 的具体版本。如果可以取得特定 commit，不应只用不断变化的 main 分支作为唯一版本依据。

- Current: style guide v2.0 (bilingual, from issue #12); glossary v2.0 (adds the `status` column, applies issue #11). Use the Git commit of this change as the exact reference.
