---
Name: <% tp.file.title %>
System: dnd5e
Source: 
Level: 
Level_suffix: st, nd, rd, th
School: 
Casting_Time: 
Range: 
Components: 
Duration: 
Spell_Lists: 
---
Source: <% tp.frontmatter.Source %>

_<% tp.frontmatter.Level %><% tp.frontmatter.Level_suffix %> level <% tp.frontmatter.School %>_

**Casting Time:**  <% tp.frontmatter.Casting_Time %>
**Range:** <% tp.frontmatter.Range %>
**Components:** <% tp.frontmatter.Components %>
**Duration:** <% tp.frontmatter.Duration %>


**Spell Lists.** <% tp.frontmatter.Spell_Lists %>

<% await tp.file.move("/5E/Spells/Spell Descriptions/" + tp.file.title) %>