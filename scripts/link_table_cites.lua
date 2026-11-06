-- Link "[N]" citation markers inside tables (docx / PDF builds).
-- prepare.py cannot link them in the Markdown sources (grid-table widths), so
-- this filter does it on the pandoc AST. Per chapter (everything up to the
-- next level-1 heading) the anchor prefix is read from the chapter's own
-- reference list, whose entries carry ids like "c03-ref-21".

local function prefix_of(blocks)
  local prefix
  for _, b in ipairs(blocks) do
    pandoc.walk_block(b, {
      Span = function(s)
        local p = s.identifier:match("^c(%d+)%-ref%-%d+$")
        if p then prefix = prefix or p end
      end,
    })
  end
  return prefix
end

local function link_table(tbl, prefix)
  return pandoc.walk_block(tbl, {
    Str = function(s)
      if not s.text:find("%[%d+%]") then return nil end
      local out, pos = {}, 1
      while true do
        local a, b, n = s.text:find("%[(%d+)%]", pos)
        if not a then break end
        if a > pos then out[#out + 1] = pandoc.Str(s.text:sub(pos, a - 1)) end
        out[#out + 1] = pandoc.Link(pandoc.Str("[" .. n .. "]"), "#c" .. prefix .. "-ref-" .. n)
        pos = b + 1
      end
      if pos <= #s.text then out[#out + 1] = pandoc.Str(s.text:sub(pos)) end
      return out
    end,
  })
end

function Pandoc(doc)
  local segments, cur = {}, {}
  for _, b in ipairs(doc.blocks) do
    if b.t == "Header" and b.level == 1 and #cur > 0 then
      segments[#segments + 1] = cur
      cur = {}
    end
    cur[#cur + 1] = b
  end
  segments[#segments + 1] = cur

  local blocks = {}
  for _, seg in ipairs(segments) do
    local prefix = prefix_of(seg)
    for _, b in ipairs(seg) do
      if prefix and b.t == "Table" then b = link_table(b, prefix) end
      blocks[#blocks + 1] = b
    end
  end
  doc.blocks = blocks
  return doc
end
