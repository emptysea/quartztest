---
Name: <% tp.file.title %>
System: dnd5e
Source: 
Level: 0
School: 
Casting_Time: 
Range: 
Components: 
Duration: 
Spell_Lists: 
---
Source: <% tp.frontmatter.Source %>

_<% tp.frontmatter.School %> cantrip_

**Casting Time:**  <% tp.frontmatter.Casting_Time %>
**Range:** <% tp.frontmatter.Range %>
**Components:** <% tp.frontmatter.Components %>
**Duration:** <% tp.frontmatter.Duration %>


**Spell Lists.** <% tp.frontmatter.Spell_Lists %>

<% await tp.file.move("/5E/Spells/Spell Descriptions/" + tp.file.title) %>