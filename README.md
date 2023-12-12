# book recommendation


## Dataset information (after drop,..)

**Users**

**Books**

| Trường       | note                  |
|--------------|-----------------------|
| bookURL      | url                    |
| title        | NLP                   |
| description  |                       |
| author       | categorical variable  |
| genres       |                       |
| language     |                       |
| ratingCounts | numberic              |
| reviewCounts |                       |
| avgRating    |                       |
| ratingHistogram|                       |
| pageNumber   |                       |
| publicYear   |                       |

**Interactive**

| Trường       | note                  |
|--------------|-----------------------|
| bookURL      | url                   |
| userId       |                       |
| rating       | 0 -> 5                |
| review       | NLP                   |



## TODO
== Nhungdt
- [ ] crawl data
  - [x] books
  - [ ] interactives
- [ ] NLP

== DuongDq
- [ ] convert to Categorical variable
- [ ] rating -> numberic
- [ ] translate review to English, remove specific characters, meaningless words 
- [ ] rating hisrogram 
- [ ] public second :) -> year