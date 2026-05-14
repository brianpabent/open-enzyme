-- Pandoc Lua filter: allow line breaks inside inline-code monospace text.
--
-- Problem: pandoc renders `inline code` as \texttt{...}. Inside \texttt,
-- LaTeX cannot break lines, so long monospace strings (file paths, URLs,
-- script names) overflow their containing box. In body prose this runs
-- past the right margin; in table cells it visually overlaps the adjacent
-- cell's content.
--
-- Fix: replace each inline Code element with a raw LaTeX \texttt{...} that
-- has \allowbreak{} inserted after each separator character (/, -, ., _).
-- LaTeX prefers actual line ends but will use these allowed break points
-- when no other option fits. The result: long paths break at slash
-- boundaries inside the cell, no cross-cell visual overlap.
--
-- Only applied to Code elements with at least one separator character,
-- because short code spans without separators don't have an overflow
-- problem and don't need the (slightly more verbose) emitted LaTeX.

local SEPARATORS = "[/%-%._]"

local function latex_escape(s)
  -- Escape LaTeX special characters that can appear inside \texttt{}.
  s = s:gsub("\\", "\\textbackslash{}")
  s = s:gsub("([{}#%$&%%])", "\\%1")
  s = s:gsub("_", "\\_")
  s = s:gsub("~", "\\textasciitilde{}")
  s = s:gsub("%^", "\\textasciicircum{}")
  return s
end

function Code(el)
  local text = el.text
  if not text:find(SEPARATORS) then
    return nil  -- no break opportunities to add; let pandoc render normally
  end

  -- Escape LaTeX specials, then inject \allowbreak{} after each separator.
  local escaped = latex_escape(text)
  local broken = escaped:gsub("(" .. SEPARATORS .. ")", "%1\\allowbreak{}")

  return pandoc.RawInline("latex", "\\texttt{" .. broken .. "}")
end
