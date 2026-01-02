r'''

For the (very good) original documentation, go [here](https://pdoc.dev/docs/pdoc.html).

In general I try to use markup notiation with a little HTML, to keep it simple.

# Run pdoc

``` shell
pdoc '.\My Module A\' -o .\docs

# If source shall not be integrated / shown within the HTML
pdoc '.\My Module A\' --no-show-source -o .\docs
```

# Structure (headings, lists)
Elements to structure the content.

## Headings
Just hashtags:

```
# Heading First Level
Some text ...

## Heading Second Level
More text ...

### Heading Third Level
And even more text ...
```
Headings of first and second level are shown within the contents on the left.
<img src="./Header.png", height = 200>

## Lists
Just dashs and tabs ...
```
- Entry 1
    - Entry 1.1
- Entry 2
- Entry 3
    - Entry 3.1
        - Entry 3.1.1
```
... to get this:
- Entry 1
    - Entry 1.1
- Entry 2
- Entry 3
    - Entry 3.1
        - Entry 3.1.1

# Includes and images

## Includes
Use the code below without the hashtag. I only add the hashtags, so the include directive will not be executed.
```
# Include a whole file:
# .. include:: ./fileToInclude.txt

# Include only parts of a file:
# .. include:: ../fileToInclude.txt
#   :start-line: 1
#   :end-before: Changelog
```
Helpful options
- start-line
- end-line
- start-after
- end-before

[further options see here](https://docutils.sourceforge.io/docs/ref/rst/directives.html#including-an-external-document-fragment)

## Images
I tried to use ".. image:: example.png" to include images. It did not work. I use ...
```
<img src="./example.png", height = 200>
```

# References
```
# Define the reference somewhere in the file ...
[Link to web]: https://www.google.com/
[Link to file]: ./my pdoc cheat sheet.html
[Link to section in file]: ./my pdoc cheat sheet.html#structure-headings-lists

# ... and use it somewhere else in the file.
[Link to web][]
[Link to file][]
[Link to section in file][]
```

[Link to web]: https://www.google.com/
[Link to file]: ./my pdoc cheat sheet.html
[Link to section in file]: ./my pdoc cheat sheet.html#structure-headings-lists

- [Link to web][]
- [Link to file][]
- [Link to section in file][]

Other variant
```
[Link](./my pdoc cheat sheet.html#structure-headings-lists)
```
[Link](./my pdoc cheat sheet.html#structure-headings-lists)

# Further commands
To move text into a new line, use `<br>`.

'''
