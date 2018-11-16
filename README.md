# Django Testing

Pre-requiste before we start
1. Python 2.7
2. Django 1.1
3. Selenium 3.1
4. Git hub repository
5. OS (prefered, Ubuntu 16.04)

# Things to Know

1. Install python and verify the version (2.7)
2. Install pip and virutal environment
3. Create virtual environment
4. Activate the virtual environment
5. pip install all the packages needed (Django, selenium, pytest)
6. 


## Complete process steps of the project in brief

1. Inputs are either PDFs or Images which are uploaded by **end user**

2. If files uploaded are PDFs, those are converted to images using **imagemagic/wand** library

3. These Images to undergo **pre-processing technique** 

4. This technique removes noise, skew, rotation, super resolution on the images

4. Once pre-processing technique is complete, multiple page single file image are converted into one single image

5. Imagess now undergoes OCR mechanism performed either by **tessaract** or **ocrmypdf** OCR Engine

    * For terrasact OCR Engine: Inputs are images, but the output can be text/pdf files

            | Left-aligned | Center-aligned | Right-aligned |
            | :---         |     :---:      |          ---: |
            | git status   | git status     | git status    |
            | git diff     | git diff       | git diff      |

    * For ocrmypdf OCR Engine: Inputs are PDFs, but the output can be text/pdf files

            | Input | Output |
            | :---: | :---:  |
            | .pdf | .txt |
            | .pdf | .pdf |

5. OCR mechanism returns the output in **PDF** for further processing

6. PDFs are OCRized and are now used to extract the data points information as per the business requirement

6. Once data points are extracted, those are shown on the UI & user can verify/edit/delete datapoint accordingly
