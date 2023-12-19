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

**Nhungdt**
- [ ] crawl data
  - [x] books
  - [ ] should we just crawl the listed columns (*Books* table) ?
  - [ ] interactives
- [ ] clean data
  - [ ] look for any Missing Data
  - [ ] populate or remove Missing Data
- [ ] NLP

**DuongDQ**
- [ ] clean data
  - [ ] convert to Categorical variable
  - [ ] rating -> numeric
  - [ ] translate review to English, remove specific characters, meaningless words 
  - [ ] rating hisrogram 
  - [ ] public year -> categoty
- [x] check data loaded, dimensions, info, ...

**Phuongvt**
- [ ] look for any distinct values in Categorical columns
- [ ] data understanding by Visualization 
  - [ ] Phượng tự thêm vào nhé
  - [ ] 
  (Correlation - shows relataion of Numerical columns  
    Chi-Square - shows relation of Categorical columns )

**Các idols**
