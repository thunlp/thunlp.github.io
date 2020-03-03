# thunlp.github.io

## FewRel Evaluation

### Pipeline of Adding A New Record

First, add a new line in `1/meta.csv` for 1.0 (or `2/meta_da.csv`, `2/meta_nota.csv` for 2.0)

Each line of the records should contain 9 items, seperated by **tab** `\t`. 9 items are: `name`, `paper link`, `code link`, `institute`, `date`, `performance 1,2,3,4`.
If the item is void (e.g., no paper link is provided), use empty string. See `1/meta.csv` for example.

Then, run `1/build_html.ipynb` in jupyter notebook (or `2/build_html_da.ipynb`, `2/build_html_nota.ipynb`) to get the sorted html result (sorted by average performance over four entries). Then copy/paste it in the `1/fewrel1.html` (or corresponding 2.0 html).
The correct location has been highlighted by script `<!-- Note: add result here. -->`. Remember to overwrite the old results.

When an anonymous request comes, you need to come up with an anonymous name (e.g., `Anonymous Rabbit`).
Make sure it is not conflict with previous names.
All anonymous names and their corresponding emails should be recorded in the google doc.
