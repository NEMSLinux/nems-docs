# nems-docs
Documentation for NEMS Linux.

This documentation will inevitably replace our tired old wiki. Currently, you can review the live version of this repository at https://docs2.nemslinux.com/

## Helpful Resources

I'm actually new to Restructured Text, though I see similarities to some of the Discord markdown. So having some resources to help find quick syntax forumulae can be helpful. Here are some that I've turned to for help:

- General structure / syntax, a good overall guide: https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html
- Specifically helpful when customizing Admonition Boxes: https://docutils.sourceforge.io/docs/ref/rst/directives.html
- Links: https://sublime-and-sphinx-guide.readthedocs.io/en/latest/references.html

## Guidelines

As I would like the documentation to have a consistent look throughout, please follow these guidelines for your edits. You are also welcome to add to these guidelines if you have a suggestion for certain layouts.

### Layout

#### Images

When embedding an image, please place the image in /img and use the following format:

```
.. figure:: ../../img/relative_filename.jpg
  :width: 600
  :align: center
  :alt: Alt text describing image goes here

  Caption goes here
```

Image files need to be JPG or PNG. Sadly, ReadTheDocs doesn't appear to support WebP (they don't show up).

#### Step-By-Step Instructions

When including step-by-step instructions, please use number lists at the top level and second level in such a way that future readers may refer to the instruction as, for example, 2.3 (the 2nd list, 3rd item). If you desire to include images within the steps, you will need to pay particular attention to how this impacts your automated numbering (#.) and may need to switch to static numbering (1., 2., etc).

```
1. Introduction to the section.
  #. This would be step 1 (referred to as 1.1)
  #. This would be step 2 (referred to as 1.2)
  #. This would be step 3 (referred to as 1.3)
2. Introduction to the next section.
  #. Step 1 (referred to as 2.1)
  #. Step 2 (referred to as 2.2)
  #. Step 3 (referred to as 2.3)
```

If editing existing step-by-step instructions, please be particularly mindful that if the numbering changes, any previous post in the community referencing the step will now be broken. Please try to avoid such a situation if possible.

### Blocks

#### Code Block

```
.. code-block:: console

    Here is some code.
    Here is the second line of code.
    If this is the final line of code, simply have a carriage return following it.
```

#### Tip Block

```
.. Tip:: Text for the tip is here
```

#### Warning Block

```
.. Warning:: Text for the tip is here
```

#### Exercise Block

```
.. admonition:: Exercise
  :class: note
  
  Text for the exercise is here
```

