---
Location: <% tp.file.title %> 
World: 
Description:
Visited: 
Parent_Location:
---

# Description

Fill in.


# People
```dataview
table without ID file.link as person, description
from "Campaigns/<% tp.frontmatter.World %>/People"
where location = "<% tp.file.title %>"
```
# Points of Interest
```dataview
table without id file.link as location, description
where parent_location = "<% tp.file.title %>"
```
