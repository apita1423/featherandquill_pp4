# Feather & Quill

- Feather & Quill: A Bird Enthusiast's Blog.

- Feather & Quill is LIVE: [Feather & Quill](https://featherandquill-pp4-75f967db4002.herokuapp.com/)

![Feather and Quill Responsive Page](/static/readme_images/am_I_responsive.png)

---

## Table of Contents

- [Introduction](#introduction)

- [User Experience](#user-experience)

  - [Project Goals](#project-goals)
  - [Target Audience](#target-audience)

- [User Stories](#user-stories)

  - [First Time Visitor Goals](#first-time-visitor-goals)
  - [Registered User Goals](#registered-user-goals)
  - [Admin User Goals](#admin-user-goals)
  - [Agile Development](#agile-development)

- [Design](#design)

  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Imagery](#imagery)
  - [Wireframes](#wireframes)
  - [Database Relationship Schema](#database-relationship-schema)

- [Features](#features)

  - [General Features](#general-features)
  - [Future Implementation](#future-implementations)
  - [Accessibility](#accessibility)

- [Testing](#testing)

  - [HTML Validation](#html-validation)
  - [CSS Validation](#css-validation)
  - [Javascript Validation](#javascript-validation)
  - [PEP8 CI Python Validation](#pep8-ci-python-validation)
  - [Manual Testing](#manual-testing)
  - [Bugs](#bugs)

- [Tools and Technologies Used](#tools-and-technologies-used)

  - [Languages and Frameworks](#languages-and-frameworks)
  - [Libraries and Programs Used](#libraries-and-programs-used)

- [Deployment](#deployment)

  - [Heroku Deployment](#heroku-deployment)
  - [Clone Repository](#clone-repository)
  - [Fork Repository](#fork-repository)

- [Credits](#credits)
  - [Code Used](#code-used)
  - [Content](#content)
  - [Media](#media)
  - [Acknowledgments](#acknowledgments)

---

## Introduction

- Feather and Quill is my fourth project with Code Insitute. The idea for Feather and Quill came from my love for birds and books. I wanted to create a blog that will showcase the various topics between birds and books. It is a place where users can receive recommendations on books (mostly about birds), tips on bird watching, gallery of pictures that were taken, and events (future development).

---

## User Experience

### Project Goals

- Feather and Quill's goal was to create a place where users would be able to access content through blog posts about various book reviews (especially about birds), tips on bird watching for seasoned birders and beginners. Feather and Quill would also be a place where bird enthusiasts can have a conversation through comments and the possibiltiy to add pictures of their birding adventures.

### Target Audience

- The target audience for Feather and Quill is anyone who is passionate about bird watching and literature.

---

## User Stories

Not all user stories have been implemented. They have been left for future implementations.

### First Time Visitor Goals

### Registered User Goals

### Admin User Goals

### Agile Development

---

## Design

### Colour Scheme

- I wanted the colours of the site to be simple, clean, and light. I only used one colour for the buttons and footer.

![Coolors](/static/readme_images/colours.png)

### Typography

- Estonia font from [Google Font](https://fonts.google.com/?query=estonia) has been used for the Feather and Quill title.

### Imagery

- Images have been obtained from Pexel, Unsplash, Gencraft (AI), Simon & Schuster Publsihing, and Little, Brown and Company Publishing.

- All images will be credited in the [Media](#media) section.

### Wireframes

- I used Balsamiq for the wireframes for this project. At the time of creating them, I had grandieous ideas, but due to my leave of absence and limited time to create all the ideas I wanted, not everything was implemented. I tried to get as close to the original idea, but it will be a great tool to have for future updates.

### Database Relationship Schema

![Database Relationship Schema](/static/readme_images/database.png)

---

## Features

### General Features

### Future Implementation

1. An events/booking page where visitors to the page can view the events, but would not be able to book unless they are authenticated. Authenticated users can view the events and book for the event.
2. Authicated users would be able to comment anonoymously to blog posts.
3. A newsletter that can be set to authenticated user about events happening in the month, which helps if they are not on the site often.

### Accessibility

---

## Testing

### HTML

### CSS
CSS code was tested using [W3C CSS Validator](https://jigsaw.w3.org/css-validator/). Passed and no errors found.
![CSS Validation](/static/readme_images/css_validation.png)

### Javascript
JS code was tested using [JSHint Validator](https://jshint.com/). Code was used for timeout of messages. Although two errors were found the functionality of the timeout worked perfectly.
![JS Validation](/static/readme_images/js_validation.png)

### PEP8 CI Python
Python code was tested using [CI Python Linter](https://pep8ci.herokuapp.com/). The only error was in the urlpatterns in urls.py in birdblog. The line exceeded the length, but there wasn't a way to shorten without it giving me another error.
![CI Python Linter](/static/readme_images/python_validation.png)

| App | Comments | Pass/Fail | 
| --- | --- | --- |
| about | all files passed with no errors | PASS |
| photos | all files passed with no errors | PASS |
| birdblog | Two path exceeded the line length, but I was unable to fix due to giving another error | PASS |

### Manual Testing

### Bugs

---

## Tools and Technologies Used

### Languages Used

- HTML
- CSS
- Javascript
- Python

### Frameworks Used

- Django
- Crispy Forms
- Bootstrap 5
- Cloudinary

### Database Used

- ElephantSQL

### Tools

- VSCode - IDE Used.
- Github - To store the Feather and Quill repository.
- Font Awesome - For the social links and heart in the footer.
- Balsamiq - Used to create the wireframes for the project.
- Favicon - Used to create the favicon for the site.
- Google Font - Estonia font used for the title of the site.
- Bootswatch - For bootstrap template
- Heroku - Cloud platform used for deployment of the project.
- Pexel - Images used for gallery and blog.
- Unsplash - Images used for gallery and blog.
- Gencraft - Creation of two AI images for the title page and blog posts main image.
- ChatGPT - Content for the blog posts and About Us section.
- DrawSQL - Site for the creation of the database relationship diagram.
- Coolors - Used to find colour for the website.

---

## Deployment

- Feather & Quill has been deployed through Heroku.

- Click Here for the Live Site: [Feather & Quill](https://featherandquill-pp4-75f967db4002.herokuapp.com/)

### Heroku Deployment

### Clone Repository

### Fork Repository

---

## Credits

### Code Used

- I relied on CI's I Think Therefore I Blog walkthrough for the bases of the my project.

- Dennis Ivy's Photo Album App with Django & S3 Buckets YouTube tutorial (I did not use S3 Buckets) helped me create the photo app [Dennis Ivy Photo Album App](https://www.youtube.com/watch?v=sSquD2u5Ie0)

- For the 404 page, I looked through this website [404 Page](https://www.makeuseof.com/create-custom-404-error-page-django/).

- I also used Dave Gray's YouTube tutorial to become more familiar with Django. [Dave Gray Django Tutorial](https://www.youtube.com/playlist?list=PL0Zuz27SZ-6NamGNr7dEqzNFEcZ_FAUVX)

### Content

- Content for blog posts and about us page has been sourced from [ChatGPT](https://chat.openai.com/auth/login). The content has been checked and various addition of sentences where I felt was necessary was used.

### Media

Images have been sourced from Pexel, Unspash, Gencraft AI, Simon & Schuster Publsihing, and Little, Brown and Company Publishing.

Two images for the book reviews on the blog post has been taken from their publishing company. A link to the publishing company of each book has been added to the relative blog post.

- [The Goldfinch](https://www.hachettebookgroup.com/titles/donna-tartt/the-goldfinch/9780316055437/?lens=little-brown)
- [An Enchantment of Ravens](https://www.simonandschuster.com/books/An-Enchantment-of-Ravens/Margaret-Rogerson/9781481497596)

Images sourced from Pexel:

- [Bird Image 1](https://www.pexels.com/photo/birds-feeding-on-bird-seeds-6702248/)
- [Bird Image 2](https://www.pexels.com/photo/closeup-photography-of-white-and-brown-owl-1310787/)
- [Bird Image 3](https://www.pexels.com/photo/a-low-angle-shot-of-birds-flying-in-the-sky-between-trees-at-the-forest-14686220/)
- [Bird Image 4](https://www.pexels.com/photo/selective-focus-photography-of-vintage-brown-and-gray-coffee-grinder-1309778/)
- [Bird Image 5](https://www.pexels.com/photo/bokeh-lights-67088/)

Images sourced from Unsplash:

- [Bird Image 6](https://unsplash.com/photos/black-binoculars-on-opened-book-S8wI7myzAjE)

Images sourced from Gencraft AI:

- [Bird Image 7](https://gencraft.com/prompt/85c15f30-f465-4a69-8b43-a31d7860d4fa?creation_id=2dc2a55c-1370-4969-93b4-df6f1d420f4c)

### Acknowledgments

- I'm extremely grateful for my mentor Martina, who has gone through countless of questions and has guided me through all of them.

- Thomas from Tutor Support that helped me with two issues that I thought was a neverending story.

- I'm also greateful for my husband, who has encouraged me to keep on going especially with this project, which has given me multiple issues.
