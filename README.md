# book recommendation


## Dataset information (after drop,..)

**Users**

**Books**

| Trường       | note                  |
|--------------|-----------------------|
| bookURL      |                     |
| title        | NLP                   |
| description  |                       |
| author       |   |
| genres       | categorical variable     |
| language     | categorical variable   |
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

**Nhungdt**
- [x] crawl data
  - [x] books
  - [ ] should we just crawl the listed columns (*Books* table) ?
  - [ ] interactives
- [ ] NLP

**DuongDQ**
- [x] check data loaded, dimensions, info, ...
- [x] clean data
  - [x] convert to Categorical variable
  - [x] rating -> numeric
  - [x] translate review to English, remove specific characters, meaningless words 
  - [x] rating hisrogram 
  - [x] public year
  - [x] look for any Missing Data
  - [x] populate or remove Missing Data
- [ ] look for any distinct values in Categorical columns
**Phuongvt**
- [ ] data understanding by Visualization 
  - [ ] Phượng tự thêm vào nhé
  - [ ] 
  (Correlation - shows relataion of Numerical columns  
    Chi-Square - shows relation of Categorical columns )
