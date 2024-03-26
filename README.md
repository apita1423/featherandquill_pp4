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

- [User Story - Comment anonymously](https://github.com/apita1423/featherandquill_pp4/issues/10)
- [User Story - Like Blog Posts](https://github.com/apita1423/featherandquill_pp4/issues/9)
- [Admin Story - Create a schedule of events](https://github.com/apita1423/featherandquill_pp4/issues/5)
- [Admin Story - Create a booking form for events](https://github.com/apita1423/featherandquill_pp4/issues/4)

### User Visitor Goals

<details>
<summary>First Time User</summary>
<ul>
<li> As a FIRST TIME USER I can ONLY SEE THE HOME, ABOUT US, LOGIN, SIGN UP PAGE so that LEARN ABOUT THE SITE AND JOIN</li>
<li> AC 1 - GIVEN - User is first time visitor to the site. </li>
<li> AC 2 - WHEN - On the home page, only home, about us, login, and sign up is in the nav bar.</li>
<li> AC 3 - THEN - User can click on Join Now in the home page or sign up page.</li>
</ul>
</details>

<details>
<summary>Visitor User</summary>
<ul>
<li> As a VISITOR USER I can REGISTER/SIGNUP so that I CAN POST COMMENTS ON BLOG POSTS THAT I'M INTERESTED IN.</li>
<li> AC 1 - GIVEN I am a visitor user </li>
<li> AC 2 - AND I click on the sign up button</li>
<li> AC 3 - AND I add a username and password (email optional)</li>
<li> AC 4 - WHEN I click on the Sign Up button</li>
<li> AC 5 - THEN I am redirected to home page showing a list of blog posts</li>
</ul>
</details>

### Registered User Goals

<details>
<summary>User Story - Login</summary>
<ul>
<li> As a REGISTERED USER I can LOGIN INTO MY ACCOUNT so that I CAN COMMENT ON BLOG POSTS ON THE SITE.</li>
<li> AC 1 - GIVEN I am a registered user</li>
<li> AC 2 - AND I click on login</li>
<li> AC 3 - WHEN I enter my username and password</li>
<li> AC 4 - AND I click on the login button</li>
<li> AC 5 - THEN It redirects to login home page showing the list of posts</li>
</ul>
</details>

<details>
<summary>User Story - View Blog Posts</summary>
<ul>
<li> As a REGISTERED/ADMIN USER I can VIEW THE LIST OF BLOG POSTS so that I CAN VIEW AND CLICK ON POSTS.</li>
<li> AC 1 - GIVEN I am a registered/admin user.</li>
<li> AC 2 - WHEN I am on the blog page.</li>
<li> AC 3 - THEN I can view a list of blog posts.</li>
</ul>
</details>

<details>
<summary>User Story - Comment on posts</summary>
<ul>
<li> As a REGISTERED USER I can LEAVE COMMENTS ON BLOG POSTS so that START OR BE PART OF A CONVERSATION.</li>
<li> AC 1 - GIVEN I am a registered user</li>
<li> AC 2 - AND I am logged in</li>
<li> AC 3 - WHEN I am in a blog post</li>
<li> AC 4 - THEN I can add comment</li>
</ul>
</details>

<details>
<summary>User Story - Update/Delete Comments</summary>
<ul>
<li> As a REGISTERED USER I can UPDATE OR DELETE COMMENTS so that I CAN EITHER UPDATE OR DELETE COMMENTS THAT ARE NOT OF INTEREST OR NEED UPDATING.</li>
<li> AC 1 - GIVEN I'm a registered user</li>
<li> AC 2 - AND I'm logged in</li>
<li> AC 3 - THEN I can update or delete my own comments.</li>
</ul>
</details>

<details>
<summary>User Story - View/Add pictures in gallery</summary>
<ul>
<li> As a USER/ADMIN I can I CAN VIEW AND ADD PICTURES TO GALLERY so that PHOTOS CAN BE SEEN BY OTHER REGISTERED USERS</li>
<li> AC 1 - GIVEN I am a registered user</li>
<li> AC 2 - AND I am logged in</li>
<li> AC 3 - WHEN I click on Add Photos</li>
<li> AC 4 - THEN I can add photos, a category, and description</li>
<li> AC 5 - THEN I can view the photo that has been added</li>
</ul>
</details>

### Admin User Goals

<details>
<summary>Admin User - Create Blog Posts</summary>
<ul>
<li> As a ADMIN I can CREATE, READ, UPDATE, DELETE BLOG POSTS so that THEY CAN BE VIEWED BY REGISTERED AND UNREGISTERED USERS.</li>
<li> AC 1 - GIVEN I am an admin user</li>
<li> AC 2 - AND I am logged in</li>
<li> AC 3 - THEN I can create blog posts</li>
<li> AC4 - THEN I can read blog posts</li>
<li> AC 5 - THEN I can update blog posts</li>
<li> AC6 - THEN I can delete blog posts</li>
</ul>
</details>

<details>
<summary>Admin User - Draft Blog Posts</summary>
<ul>
<li> As a ADMIN I can DRAFT BLOG POSTS so that I CAN HAVE CONTENT READY FOR FUTURE POSTS.</li>
<li> AC 1 - GIVEN I am an admin user</li>
<li> AC 2 - AND I am logged in</li>
<li> AC 3 - WHEN I create a blog post</li>
<li> AC 4- THEN I can save it has a draft to be viewed/edited/post in the future</li>
</ul>
</details>

<details>
<summary>Admin User - Review/A(Dis)pprove/ Comments</summary>
<ul>
<li> As a ADMIN I can REVIEW, APPROVE, DISAPPROVE COMMENTS so that THE COMMENTS CAN BE VIEWED BY REGISTERED AND UNREGISTERED USERS.</li>
<li> AC 1 - GIVEN I am a admin user</li>
<li> AC 2 - AND I am logged in</li>
<li> AC 3 - AND I see a list of pending comments</li>
<li> AC 4 - WHEN I review the pending comments</li>
<li> AC 5 - THEN I can approve or disapprove the comments</li>
</ul>
</details>

### Agile Development
- The agile methodology was the main project management tool to use for Feather and Quill. For milestones, I used five epics as way to bundle the user stories: **Comments**, **Blog Posts**, **Gallery**, **Events**, **README**. A Kanban project was also used with four different title: **Todo**, **In Progress**, **Done**, and **Future**. The MoSCoW Method labels for also used: **must have**, **should have**, **could have**, and **wont have**. Other labels were also used: **CRUD** and **documentation**.

#### Kanban
- Kanban board was split into four sections: Todo, In Progress, Done, and Future. I decided to add a future section to put the User Stories that were labelled could have and wont have, which will be for future implementations.
![Kanban Board](/static/readme_images/kanban.png)

#### Milesstones
- I decided to create the EPICs as milestones due to the side of the project and time. There are five epic milestones I used: Comments, Blog Posts, Gallery, Events, and README. All the user stories corresponded with the epic milestones.
![Milestones](/static/readme_images/milestones.png)

### MoSCoW Method Labels
- The MoSCow Method labels I used were: must-have, should-have, could-have, and wont-have. I added two extra labels named CRUD and documentation. The CRUD labels was to quickly identify which user stories would have the CRUD functionality and documentation was made for the README.
![MoSCoW Method Labels](/static/readme_images/labels.png)

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

<details><summary>Home/Landing Page</summary>
<img src="/static/wireframes_images/home_wf.png">
</details>

<details><summary>About Us Page</summary>
<img src="/static/wireframes_images/about_us_wf.png">
</details>

<details><summary>Blog Page</summary>
<img src="/static/wireframes_images/blog_wf.png">
</details>

<details><summary>Blog Post/Comments</summary>
<img src="/static/wireframes_images/blogpost_wf.png">
</details>

<details><summary>Gallery</summary>
<img src="/static/wireframes_images/gallery_wf.png">
</details>

<details><summary>Gallery Add Image</summary>
<img src="/static/wireframes_images/gallery_form_wf.png">
</details>

<details><summary>Gallery View Image</summary>
<img src="/static/wireframes_images/gallery_view_wf.png">
</details>

<details><summary>Login Page</summary>
<img src="/static/wireframes_images/login_wf.png">
</details>

<details><summary>Sign Up Page</summary>
<img src="/static/wireframes_images/signup_wf.png">
</details>

### Database Relationship Schema
![Database Relationship Schema](/static/readme_images/database.png)

---

## Features

### General Features

<details><summary>Favicon Image</summary>
<img src="/static/readme_images/favicon.png">
</details>

<details><summary>Favicon Tab</summary>
<img src="/static/readme_images/favicon_tab.png">
</details>

<details><summary>Title/Navbar</summary>
<img src="/static/readme_images/title_navbar.png">
</details>

<details><summary>Landing/Home Page</summary>
<img src="/static/readme_images/landing_home_page.png">
</details>

<details><summary>About Us</summary>
<img src="/static/readme_images/aboutus.png">
</details>

<details><summary>Sign Up</summary>
<img src="/static/readme_images/signup.png">
</details>

<details><summary>Login</summary>
<img src="/static/readme_images/login.png">
</details>

<details><summary>Login/Sign Up Navbar</summary>
<img src="/static/readme_images/login_navbar.png">
</details>

<details><summary>Gallery Paqe</summary>
<img src="/static/readme_images/gallery_page.png">
</details>

<details><summary>Gallery View</summary>
<img src="/static/readme_images/gallery_view.png">
</details>

<details><summary>Gallery Filter</summary>
<img src="/static/readme_images/gallery_filter.png">
</details>

<details><summary>Gallery Filter - No Photo</summary>
<img src="/static/readme_images/gallery_no_filter.png">
</details>

<details><summary>Gallery Add Photo</summary>
<img src="/static/readme_images/gallery_add_photo.png">
</details>

<details><summary>Blog Post List Page</summary>
<img src="/static/readme_images/blog_post_list.png">
</details>

<details><summary>Blog Post</summary>
<img src="/static/readme_images/blogpost.png">
</details>

<details><summary>Blog Comment</summary>
<img src="/static/readme_images/blog_comment.png">
</details>

<details><summary>Blog Comment CRUD</summary>
<img src="/static/readme_images/blog_comment_crud.png">
</details>

<details><summary>Blog Comment Delete Prompt</summary>
<img src="/static/readme_images/blog_comment_delete.png">
</details>

<details><summary>Blog Post Paginated NEXT</summary>
<img src="/static/readme_images/blogpost_paginated_next.png">
</details>

<details><summary>Blog Post Paginated PREV</summary>
<img src="/static/readme_images/blogpost_paginated_prev.png">
</details>

<details><summary>Logout Prompt</summary>
<img src="/static/readme_images/logout_prompt.png">
</details>

<details><summary>Error 404 Page</summary>
<img src="/static/readme_images/error404_page.png">
</details>

<details><summary>Footer</summary>
<img src="/static/readme_images/footer.png">
</details>

### Future Implementation

1. An events/booking page where visitors to the page can view the events, but would not be able to book unless they are authenticated. Authenticated users can view the events and book for the event.
2. Authicated users would be able to comment anonoymously to blog posts.
3. A newsletter that can be set to authenticated user about events happening in the month, which helps if they are not on the site often.

### Accessibility

---

## Testing

### HTML
HTML code was tested using [W3C HTML Validator](https://validator.w3.org/).


### CSS
CSS code was tested using [W3C CSS Validator](https://jigsaw.w3.org/css-validator/). Passed and no errors found.
![CSS Validation](/static/readme_images/css_validation.png)

### Javascript
JS code was tested using [JSHint Validator](https://jshint.com/). Code was used for timeout of messages. Although two errors were found the functionality of the timeout worked perfectly.
![JS Validation](/static/readme_images/js_validation.png)

### PEP8 CI Python
Python code was tested using [CI Python Linter](https://pep8ci.herokuapp.com/). The only error was in the urlpatterns in urls.py in birdblog. The line exceeded the length, but there wasn't a way to shorten without it giving me another error.

**Update** After running the CI Python Linter and deploying the project there was an error with the syntax in th models.py files in birdblog and photos. To fix it I had to bring the code back to the exceeded amount for the error to go away and the project to deploy.
![CI Python Linter](/static/readme_images/python_validation.png)

| App | Comments | Pass/Fail | 
| --- | --- | --- |
| about | all files passed with no errors | PASS |
| photos | files passed with no error exception the models.py where it was giving an syntax error | PASS/WARNING |
| birdblog | Two path exceeded the line length, but I was unable to fix due to giving another error. Also same error has in photos app.| PASS/WARNING |

### Manual Testing

| USER STORY | GHERKIN | PASS/FAIL | 
| --- | --- | --- |
| As a FIRST TIME USER I can ONLY SEE THE HOME, ABOUT US, LOGIN, SIGN UP PAGE so that LEARN ABOUT THE SITE AND JOIN |
| | AC 1 - GIVEN - User is first time visitor to the site.|
| | AC 2 - WHEN - On the home page, only home, about us, login, and sign up is in the nav bar.|
| | AC 3 - THEN - User can click on Join Now in the home page or sign up page.| PASS |

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

1. Go to heroku.com and login with your credentials. 
2. Sing in with your multifactor pin.
3. Select 'New'.
4. Create a unique name (it should turn green if the name is available), and select the location.
5. Once the app is created, click on 'Reveal Config Vars'
    - DATABSE_URL
    - SECRET_KEY
    - PORT = 8000
    - DISABLE_COLLECTSTATIC = 1 (DISABLE FOR PRODUCTION)
    - CLOUDINARY_URL
6. Under the 'Deploy' button, connect to your GitHub repository.
7. Once connected pick the repository that you will want to connect to.
8. Under 'Manual Deploy', click on Deploy Branch.
9. Once manual deployment is successful click on 'View' or scroll up and click on 'Open app'.

### Clone Repository

1. In the GitHub repository, click 'Code' and with HTTPS underline copy the link.
2. Open git bash and change the working directory to the intented location.
3. Type git clone and paste the link.
4. Press enter to start the creation of a local clone repository.

### Fork Repository

1. In the Github repository, click 'Fork' and then 'Create a Fork'.
2. Change the name and description of the fork.
3. Select to copy only the main branch or all braches.
4. Click 'Create a Fork'. 
5. A newly created repository will appear in you Github repository.

---

## Credits

### Code Used

- I relied on CI's I Think Therefore I Blog walkthrough for the bases of the project.

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
- [Bird Image 6](https://www.pexels.com/photo/assorted-books-626986/)
- [Bird Image 7](https://www.pexels.com/photo/crop-unrecognizable-tourist-taking-photo-with-photo-camera-in-mist-4339449/)
- [Bird Image 8](https://www.pexels.com/photo/close-up-of-a-seagull-sitting-on-a-wall-near-the-shore-15971438/)

Images sourced from Unsplash:

- [Bird Image 9](https://unsplash.com/photos/black-binoculars-on-opened-book-S8wI7myzAjE)

Images sourced from Gencraft AI:

- [Bird Image 10](https://gencraft.com/prompt/85c15f30-f465-4a69-8b43-a31d7860d4fa?creation_id=2dc2a55c-1370-4969-93b4-df6f1d420f4c)

### Acknowledgments

- I'm extremely grateful for my mentor Martina, who has gone through countless of questions and has guided me through all of them.

- Thomas from Tutor Support that helped me with two issues that I thought was a neverending story.

- I'm also greateful for my husband, who has encouraged me to keep on going especially with this project, which has given me multiple issues. Also, to my two cats and dog that have kept me company through the past weeks.
