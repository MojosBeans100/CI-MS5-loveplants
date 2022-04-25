# Love Plants
Love Plants is a Full Stack B2C (business to customer) e-commerce website which allows customers to view and purchase products related to plants. The website was developed for Milestone 5 as part of the Code Institute Diploma in Software Development. 

![Responsive website](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1650050038/LovePlants/ReadMe/amirespoinve_twskbo.jpg)

# Table of contents
- [Love Plants](#love-plants)
- [Project Overview](#project-overview)
- [UX](#ux)
    * [Strategy](#strategy)
        + [Site user goals](#site-user)
        + [Admin user goals](#admin-user)
        + [User stories](#user-stories)
    * [Scope](#scope)
        + [Sprints](#sprints)
        + [Epics, Issues, Tasks](#sprints)
        + [Scope Creep](#scope-creep)
        + [Requirements](#requirements)
    * [Structure](#structure)
        + [Interaction Design (IXD)](#interaction-design)
        + [Information Architecture (IA)](#information-architecture)
    * [Skeleton]
    * [Surface]

    * [Structure](#structure)
        + [Pages](#pages)
        + [Database](#database)
            - [Models](#models)
    * [Style](#style)
        + [Wireframes](#wireframes)
        + [Font](#font)
        + [Colours](#colours)
        + [Layout](#layout)

- [Features](#features)
    * [Homepage](#homepage)
    * [Discover](#discover)
    * [My Pipelines](#pipelines)
    * [Detail view](#detail)
    * [Create Pipeline](#create-a-pipeline)
    * [Edit](#edit-pipeline)
    * [Delete](#delete-pipeline)
    * [Error pages](#error-pages)
- [Technologies used](#technologies-used)
    * [HTML/CSS](#htmlcss)
    * [Javascript](#javascript)
    * [Python](#python)
    * [Django](#django)
    * [Other libraries](#other-libraries)
    * [APIs](#apis)
- [Testing](#testing)
- [Additional Features](#additional-features)
    * [UX](#ux-1)
    * [User Features](#user-features)
    * [API](#api)
- [Unfixed Bugs](#unfixed-bugs)
- [Deployment](#deployment)
- [Media](#media)
- [Credits](#credits)
- [Acknowledgements](#acknowledgements)

# Project Overview
- This website was developed for submission as the Milestone 5 project of the Code Institute Diploma in Software Development.
- The website is deployed using the Heroku pages at the following url: XXXX
- The repository on Github that contains the website source code and assets is available at the following url: XXXX
- The website was built with a responsive look and feel, designed to be enjoyable to use on all screen sizes. 

[Back to top](#love-plants)

# UX
The Five Planes - strategy, scope, structure, skeleton, and surface - method was used during the project planning phase to provide a conceptual framework for designing this e-commerce website.  The methodology for each plane is provided below. 

## Strategy
The strategy plane considers the website user's needs and the website admin's needs.

### Site User
The primary goals of the website user are as follows:
- To create an account on the website, which will allow them to purchase products
- To view the details of all products
- To add products to their shopping basket
- To proceed to checkout items in their shopping basket and receive a confirmation of the payment
- To view details relating to their account, such as order history
- To 'like' products, and add ratings and reviews to products they have bought

### Admin User
The primary goals of the website owner or admin are as follows:
- To add, edit, view and delete products
- To manage the stock quantity of products
- To view, edit and delete customer orders
- To encourage users to purchase more products
- The view and moderate customer ratings and reviews

### User Stories
All user stories are detailed in [this document](), and in the [Issues](https://github.com/MojosBeans100/CI-MS5-loveplants/issues) subfolder in the Github repository for the project.

[Back to top](#love-plants)

## Scope
The Scope plane determines the scope of the project
User Stories/Issues were mapped to Sprints (or Milestones) to plan for the current and next phase of the project. In general the Sprints were no longer than 2 weeks, and overall followed an organic order to developing an e-commerce website. 
The first sprints contained the higher priority features, providing basic website functionality to meet the project requirements (eg, allow users to checkout items).  The later sprints contained features which were not considered necessary but enhanced the project (eg, allow users to log in via social media accounts).

### Sprints
Sprint 1 - basic project set up: user authentication, create models, homepage templates, display products
Sprint 2 - the 'Bag' and 'Checkout' apps: add, edit, delete products in bag and checkout the order
Sprint 3 - the 'Profile' app: provides users more detail about their profile, order history, review products
Sprint 4
Sprint 5

### Epics, User Stories, Tasks
Epics were defined based on the main functions the website was expected to have, which mostly revolved around the main CRUD functions of the database. These Epics were refined into smaller User Stories, which could then be broken down into manageable tasks for the developer to complete within the current project iteration. User acceptance criteria was determined for each Epic/User Story

### Priority
Priority labels were assigned to each User Story/Issue, in order to determine which tasks to complete first in a Sprint. When the Issue was not completed, it could be included on another Sprint in order to complete it. 

### Scope Creep
### Requirements
Functional, content

## Structure
The Structure plane was used to plan the organisation of website functionality and navigation, to provide a clear pathway to desired user actions.  In order to facilitate the Structure plane, Interaction Design (ID) and Information Architecture (IA) were developed as below. 

### Interaction Design
The five main concerns of ID and how they were used to facilitate the Structure plane are detailed below, to create meaningful relationships within the website content and information. 

#### Consistency
Elements maintained consistency, to enable users to feel familiar with the brand of Love Plants. 

- **Colours** found on the site were deliberately minimised, since the product images provided a variety of colours.  Therefore the main two colours of the website are white and black, and additional colours are only introduced in necessary circumstances, such as to highlight form field errors. Additionally, the white/black colour palette with splashes of colour from images maintains a clean, minimalistic website. Admin users can expect to see a teal (#069b8e) color to represent elements only visible to them

- the same **font** (XXX) was used throughout the website, chosen due to it's readability and cross-platform capabilities

- **buttons** adhere to the colour consistency, with white text within a black button, and a hover effect providing the inverse style. Buttons for admin users maintain a teal hue

- where possible, **images** were kept to the same size and width to height ratio.  An example outwith this rule is on the product detail page, where it was deemed beneficial to provide a larger image

- **products** are represented with an image, a price, a rating and a product title on all pages, as this information is deemed the most appropriate to identify the product

#### Predictability
To maintain predictability for the user, standard website conventions are followed to meet users expectations, for example:

- the Love Plants logo is kept to the top left of the page, irregardless of the screen size
- the main navigation menu is placed at the top of the page, and provides only a limited selection of options so as not to overwhelm the user
- content hierarchy XXXX
- **anchor links** are styled with an underline feature on hover
- buttons represent important calls to action, such as submitting a form and maintain consistent colours as described [above](#consistency)
- as in most e-commerce sites, the top right of the page contains links to the user's profile, bag, and log in/log out facilities

#### Learnability
See below some examples of how the developer considered UX learnability when presenting the Love Plants brand, to help users achieve their goals quickly and efficiently

- use of **visuals**  as much as possible, such as icons to represent actions as opposed to text
![Icon for XXX]()

- **simplicity** in design, in effect minimising text, actions, colours.  The develop aims to only provide relevant information for the section or page, so as not cognitively overload the user with unnecessary information
![eg the checkout page provides only 1 CTA]()

- **predictable process** regarding e-commerce websites, ie look for products > select a product > add product to basket > checkout

- **prioritising primary actions**, by providing the main call to action as a button, therefore more visual to users, even though there may be other links or actions on that page.  For example, on the checkout page, users can link back to other pages, but the priority action for that page is to checkout.
![checkout button]()

#### Visibility
Decent UX/UI visibility is achieved on the website by providing obvious prompts and cues, and ensuring users are aware of all opportunities, for example:

- the navbar remains fixed to the top of the page, providing the user to opportunity to navigate to 
- users can obtain free delivery with a minimum basket total, ie by purchasing more products, and can see products which would increase their basket to this total

#### Feedback
As users have significant interaction with the site, feedback on their actions was considered important.  This was provided by:

- **in-line feedback** on forms, to emphasise invalid fields
- **notifications** on notable actions, such as adding a product to their basket.  This was achieved with Bootstrap 'toasts'
- **possible actions** available to them, 
- **communicating the context**, such as

### Information Architecture
Information Architecture, or IA, was considered when creating the structure of the website, to allow users to understand where the information they want is in relation to their current position, and to deliver the right information at the right time.  Additionally:

- the **MVC architecture pattern** provided by Django allows the website to collect, manipulate and deliver the data

- a **database schema** was used to design the database models, and to understand how they communicate with one another. (See further information on the [database]())

- **content inventory** was provided by the in-built Django Admin panel, to maintain a database of products.  This is effectively mirrored in the front-end, with a more user-friendly option for the admin to, for example, create a product

## Skeleton
### Interface Design
### Navigation Design
### Information Design
 
Facilitate the structure ie what form the structure will take
Buttons, links, navs
Icons
Data at rest - database
Data in motion - pulled from db
Data as presented 

## Surface
### Visual Design

# Database

## Database Structure
The database includes:
- Home app
- Products app
- Bag app
- Checkout app
- templates
- db.sqlite3, the local database used in development
- static, to maintain media, CSS and JS files
- manage.py, automatically created upon Django install, the command-line utility for administrative tasks
- env.py, to store environment variables and secret keys hidden from the Github repository
- .gitignore, to keep environment variables from being committed to Github
- Procfile, to allow for deployment on Heroku
- requirements.txt, to store the python packages required to run the project
- README.md, to outline the developement and purpose of this project
- TESTING.md,to outline the testing strategy used during development
- USER_STORIES.md, to list all user stories

![structure schema]()

## Models
The models created to develop this e-commerce project are defined in this section. 

![database schema]()

### User (Django context processor)
- The User model contains information about the user, as part of the [Django allauth library](https://django-allauth.readthedocs.io/en/latest/installation.html)
- No additional features are added to this model, as a basic username, email and password satisfy the requirements of the project

### Home App
The Home App serves to display the homepage for the website.  
It contains no models. 

### Profiles App
(User Stories XXX)
The Profiles App provides the user the ability to create their website profile, so they can purchase products and review their details and order history. 

### UserProfile
- The UserProfile model allows users to hold their personal information when using the site, and has a One-To-One relationship with the [User](#user-django-context-processor) model.
- The UserProfile model with be modified automatically upon the User model being modified

| Field | Description | Field type|
|-------|-------------|-----------|
|id|primary key (Django auto created|Primary Key|
|user|One-To-One field with User model|One-To-One (User)|
|default_phone_num|user's default phone number|CharField|
|default_street_address_1|user's default address|CharField|
|default_street_address_1|user's default address|CharField|
|default_town_or_city|user's default address|CharField|
|default_county|user's default address|CharField|
|default_postcode|user's default address|CharField|
|default_country|user's default address|CountryField|

### Products App
(User Stories XXX)
- The Products App serves to hold a database of products available to purchase, details about them, their categories and any reviews/ratings. 
- It contains 5 models.

#### Product
- The Product model holds information about specific products

| Field | Description | Field type|
|-------|-------------|-----------|
|id|primary key (Django auto created|Primary Key|
|category|product category|CharField|
|plant_category|if product is plant, plant category|CharField|
|name|name of the product|CharField|
|friendly_name|name of the product to be used in templates|CharField|
|latin_name|if product is plant, latin name|CharField|
|description|description of the product|TextField|
|description_source|source of the description|CharField|
|description_url|url for the description source|URLField|
|image1_source|source for the image|CharField|
|image1_source_url|url for the image|URLField|
|image2_source|source for the image|CharField|
|image2_source_url|url for the image|URLField|
|image3_source|source for the image|CharField|
|image3_source_url|url for the image|URLField|
|price|price of the product|DecimalField|
|stock_quantity|quantity of the product in stock|PositiveIntegerField|
|pot_size|diameter of the pot|PositiveIntegerField|
|height|height of the product|PositiveIntegerField|
|length|length of the product|PositiveIntegerField|
|maturity_num|maturity of the product|PositiveIntegerField|
|maturity_time|maturity of the product|CharField|
|sunlight|sunlight required for the product|CharField (choices)|
|watering|watering required for the product|CharField (choices)|
|care_required|maintenance required|CharField (choices)|
|care_instructions|any further care instructions|TextField|
|care_instructions_source|source of the care instructions|CharField|
|care_instructions_url|url of the source of the care instructions|URLField|
|rare|whether or not the product is considered rare|BooleanField|
|popular|whether or not the product is considered popular|BooleanField|
|stock|string description of whether or not the product is in stock|CharField(choices)|
|average_rating|average of all ratings the product has received|DecimalField|

#### Category
#### Plant Category

#### Recently Viewed
- The Recently Viewed model provides a short list of products the user has recently viewed (has visited the product detail page). 

| Field | Description | Field type|
|-------|-------------|-----------|
|product|the product which was recently viewed|Foreign Key (Product)|
|user|who recently viewed the product|Foreign Key (User)|
|viewed|when the user viewed the product|DateTimeField|

#### Product Review
- The Product Review model provides customer reviews and ratings about a specific product.

| Field | Description | Field type|
|-------|-------------|-----------|
|user|the authenticated user|Foreign Key (User)|
|product|the product being reviewed|Foreign Key (Product)|
|review|comments from the user who has purchased the product|TextField|
|rating|the user's rating for the product between 1 and 5|IntegerField|
|review_time|when the user left the review|DateTimeField|
|review_time_ago|how many days/weeks/months ago the user left the review|CharField|
|liked|whether the user 'likes' the product|BooleanField|

### Bag App
The Bag App serves to provide a temporary session to allow users to add products to their bag.  
It contains no models. 

### Checkout App
The Checkout App provides the structure for users to create an order and purchase products.

#### Order
- The Order model provides details about orders which the user submitted.
- This model contains several model methods to create the unique character order reference and update costs automatically.

| Field | Description | Field type|
|-------|-------------|-----------|
|order_ref|a unique 32 digit character string to provide order reference to the user|CharField|
|user_profile|the user who submitted the order|ForeignKey (UserProfile)|
|full_name|the name *of the user who submitted the order|CharField|
|email|the email *||
|phone_num|the phone number *|CharField|
|street_address_1|the street address *|CharField|
|street_address_2|the street address *|CharField|
|town_or_city|the town *|CharField|
|county|the county *|CharField|
|postcode|the postcode *|CharField|
|country|the country *|CountryField|
|date|the date and time the order was submitted|DateTimeField|
|delivery_cost|the delivery cost of the order|DecimalField|
|order_total|the total cost of all products|DecimalField|
|grand_total|the sum of the delivery_cost and order_total|DecimalField|
|original_bag|a dictionary of items in the bag and quantities|TextField|
|stripe_pid|a unique character string to communicate with Stripe|CharField|

#### OrderLineItem
- The OrderLineItem model represents details about each product in any given order (Order).
- The model contains a model method to update the lineitem_total if the quantity is changed.

| Field | Description | Field type|
|-------|-------------|-----------|
|order|the order this line item is in reference to|ForeignKey (Order)|
|product|the product on the order|ForeignKey (Product)|
|quantity|the quantity of this item on the order|IntegerField|
|lineitem_total|the total cost of this line item|DecimalField|

[Back to top](#spaceport)

### Pages
The website has five main pages, with user authentication on XXXX:
- Homepage (all users): to introduce users to the website and display purchasable products
- Products (all users): to display all products available to purchase, with sorting and filtering facilities
- Product Detail (all users): to provide additional detail about a specific product and facilities to add the product to the shopping basket
- Shopping basket (authenticated user): to display all products in a user's shopping basket
- Checkout (authenticated user): to display a form to submit payment for purchasing contents in shopping basket

The additional pages are as follows:
- Checkout Confirmation: to display details of a successful checkout
- Review/Rating: for users to delete pipelines

The website was designed to be simple, clear and uncluttered, basic in structure, and easy to navigate.
Bootstrap was used to aid responsiveness, as well as media queries in CSS.  Javascript provides interactive features to enhance user experience.




## Style

### Wireframes
Initial wireframes were designed during the project proposal stage.  During development, when more was learned about the API and it's capabilities and restrictions, the designs evolved to include more information. 

#### Homepage
![Homepage wireframe desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1647409740/LovePlants/ReadMe/Wireframes/homepage-desktop_gq7ele.png)

![Homepage wireframe desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1647409738/LovePlants/ReadMe/Wireframes/homepage-mobile_znwctr.png)

#### Products
![Products wireframe desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1647409740/LovePlants/ReadMe/Wireframes/product-list-desktop_yq6xoh.png)

![Products wireframe mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1647409740/LovePlants/ReadMe/Wireframes/product-list-mobile_apfu4a.png)

#### Product Detail
![Product detail wireframe desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1647409740/LovePlants/ReadMe/Wireframes/product-detail-desktop_blousk.png)

![Product detail wireframe mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1647409740/LovePlants/ReadMe/Wireframes/product-detail-mobile_ujpi04.png)

#### Shopping Basket
![Shopping basket wireframe desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1647409738/LovePlants/ReadMe/Wireframes/bag-desktop_akbgpk.png)

![Shopping basket wireframe mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1647409739/LovePlants/ReadMe/Wireframes/bag-mobile_jvlhka.png)

#### Checkout
![Checkout wireframe desktop]()

![Checkout wireframe mobile]()

#### Checkout Confirmation
![Checkout confirmation wireframe desktop]()

![Checkout confirmation wireframe mobile]()

#### Liked Products
![Liked products wireframe desktop]()

![Liked products wireframe mobile]()

#### Rate and Review products
![Rate/review wireframe desktop]()

![Rate/review wireframe mobile]()

#### Purchase History
![Purchase history wireframe desktop]()

![Purchase history wireframe mobile]()

#### Create Account
![Create an account wireframe desktop]()

![Create an account wireframe mobile]()

#### Log In
![Log in]()

#### Sign Out


### Font
The font style is the default Bootstrap 5 native sans-serif font stack for cross platform usability. The font remains consistent throughout the website, aside from being rendered in italic or font style for emphasis.

![Bootstrap Native Font](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1643901837/Spaceport/font_xbuoff.jpg)

### Colours
- The colours of the website are kept to basic white and black to keep the style clean and minimalistic.  Images from the products provide splashes of colour in an otherwise greyscale website. 

### Layout



[Back to top](#spaceport)

## Scope
### Site User Stories

## User Stories Strategy
Epics were defined based on the main functions the website was expected to have, which mostly revolved around the main CRUD functions of the database.  These Epics were refined into smaller User Stories, which could then be broken down into manageable tasks for the developer to complete within the current project iteration.  User acceptance criteria was determined for each Epic/User Story. See all [project iterations/boards](https://github.com/MojosBeans100/ms4-spaceport/projects).

The User Stories were designated a priority label to complete within the iteration.  The main CRUD functions were assigned a 'must-have' label.  User Stories which were deemed beneficial but not a priority were assigned a 'should-have' label.

All User Stories which were not completed had a 'could-have' label assigned to them, updated to 'won't-have' at final deployment, as they were additional features which did not affect the main functionality of the website. These User Stories could be completed if there was an opportunity for another iteration for this project.

[Back to top](#spaceport)

## User Stories
All User Stories were tested for functionality.  This is detailed in [this file](TESTING.md).

### User Story 1
As a **Site User** I can **create a pipeline**

- 1.1: As a **New/returning Site User** I can **see an introduction page to creating a pipeline** so that **I understand the restrictions**
- 1.2: As a **New/returning Site User** I can **see an advice on how to maximise my chance of my pipeline returning images** so that **I can choose my parameters accordingly**
- 1.3: As a **New Site User** I am **provided with a list of examples** so that **I have a starting point for my first pipeline**
- 1.4: As a **New/returning Site User** I am **made aware that submitting a pipeline does not guarantee results** so that **I am not disappointed if my pipeline does not receive images**
- 1.5: As a **New/returning Site User** I can **see a progress indicator on the form** so that **I know what my progress in the form is, and which sections I have completed**
- 1.6: As a **New/returning Site User** I can **see inline feedback on my form** so that **I know if the parameter I entered was incorrect**
- 1.7: As a **New/returning Site User** I can **see visual representations of relevant parameters** so that **I have a more accessible understanding of what I am selecting**
- 1.8: As a **New/returning Site User** I can **see descriptions/placeholders of parameters** so that **I know what this parameter means for my pipeline**
- 1.9: As a **New/returning Site User** I can **navigate forwards and backwards in the form** so that **I can change details before I submit**
- 1.10: As a **New/returning Site User** I can **review the details of the pipeline I have created** so that **I can review the details before I submit**
- 1.11: As a **New/returning Site User** I can **see which parameters can be changed after submission** so that **I am aware what can be edited**
- 1.12: As a **New/returning Site User** I have **feedback on submission** so that **I have confirmation that the pipeline was submitted**
- 1.13: As a **New/returning Site User** I am **redirected to the detail view of the pipeline after submission** so that **I can view the details of the pipeline I submitted**
- 1.14: As a **New/returning Site User** I am **encouraged to allow for the website to process the pipeline when first redirected** so that **I understand why the pipeline detail is initially sparse**

### User Story 2
As a **Site User** I can **view a list of all my pipelines**

- 2.1: As a **Returning Site User** I can **see the My Pipelines link on the navbar when I am logged in** so that **I can easily refer back to this at all times**
- 2.2: As a **Returning Site User** I can **see all my pipelines ordered by active status** so that **I am aware which pipelines are still active**
- 2.3: As a **Returning Site User** I can **see all my pipelines ordered by completed status** so that **I am aware which pipelines have completed all intervals**
- 2.4: As a **Returning Site User** I can **see all my pipelines ordered by pending status** so that **I am aware which pipelines I should update**
- 2.5: As a **Returning Site User** I can **see a status link section at the top of My Pipelines** so that **I can see how many pipelines are in each category, and navigate to each list separately**
- 2.6: As a **Returning Site User** I can see **a card displaying important information about each pipeline** so that **I can identify which pipeline it refers to**
- 2.7: As a **Returning Site User** I can see **a featured image on the pipeline card** so that **I know if that pipeline has found any images**
- 2.8: As a **Returning Site User** I can see **an interactive style change when I hover over a pipeline** so that **I know I can click on the pipeline card and view pipeline details**
- 2.9: As a **New Site User** I am **shown a message at the top of My Pipelines, directing me to create a pipeline** so that **when first signing up, I am linked to the next logical step**

### User Story 3
As a **Site User** I can **view all details of a specific pipeline**

- 3.1: As a **Returning Site User** I can **see that the detail view is separated into sections** so that **I can scroll to the section I am interested in**
- 3.2: As a **Returning Site User** I can **see all important and general information at the top of the detail view** so that **I can identify which pipeline it refers to**
- 3.3: As a **Returning Site User** I can **click an Update button** so that **I can refresh the details of the pipeline**
- 3.4: As a **Returning Site User** I can **see a zoomable map of the AOI in the detail view** so that **I can see the area on the Earth this pipeline refers to**
- 3.5: As a **Returning Site User** I can **see a timeline chart of my pipeline** so that **I can visualise the pipeline period, completed intervals, incomplete intervals, today's date and if/when images were found**
- 3.6: As a **Returning Site User** I can **see a table of all interval dates** so that **I can see the status of each interval**
- 3.7: As a **Returning Site User** I can **see a table of results** so that **I can easily see if images have been delivered**
- 3.8: As a **Returning Site User** I am **directed to a separate tab when I click on a found image** so that **I can view it in detail and download it**
- 3.9: As a **Returning Site User** I am **directed to a separate tab when I click on image metadata** so that **I can read it or use it in post production of the image**
- 3.10: As a **Returning Site User** I can **view the parameters I selected when creating the pipeline** so that **I am reminded of the parameters I set**
- 3.11: As a **Returning Site User** I can **see a timestamp on 'last edited'** so that **I know if/when I edited the pipeline**
- 3.12: As a **Returning Site User** I can **see buttons to edit/delete my pipeline** so that **I know how to access these functions**
- 3.13: As a **Returning Site User** I am **told if I cannot edit/delete my pipeline** so that **I am aware why these functions are/are not available**

### User Story 4
As a **Site User** I can **create an account** so that **I can log in to create pipelines, and view my pipelines**

- 4.1: As a **New Site User** I can **sign up to Spaceport** so that **I can create pipelines**
- 4.2: As a **Returning Site User** I can **log in to my account when revisiting the page** so that **I view details of my pipelines**
- 4.3: As a **Site User** I can **see the login/signup/logout link in the nav bar** so that **I am always aware of my log in state**
- 4.4: As a **Site User** I am **redirected to my pipelines when I log in** so that **my account information is immediately visible to me**
- 4.5: As a **Site User** I can **logout from my account on Spaceport** so that **my account information is kept safe and private**

### User Story 5
As a **Site User** I can **access information on satellite imagery**

- 5.1: As a **New/returning Site User** I can **see at all times the Discover page link** so that **I can always refer to this page for more information**
- 5.2: As a **New Site User** I am **firstly directed to the homepage** so that **the purpose of the site is immediately clear to me**
- 5.3: As a **New/returning Site User** I can **explore technical terms associated with satellite imagery and pipelines** so that **I can check any definitions I am unsure of**
- 5.4: As a **New/returning Site User** I am **given explanations of technical terms in the form** so that **I understand what the parameters I am setting means**
- 5.5: As a **Site User** I am **provided with links to all image metadata** so that **I can use the images in post production**
- 5.6: As a **New/returning Site User** I can **read examples of pipelines created by current/previous clients** so that **I have a context as to what I can use satellite imagery for**
- 5.7: As a **New/returning Site User** I can **read topical events involving satellite imagery** so that **I am aware of the importance of being able to access satellite imagery**
- 5.8: As a **New/returning Site User** I can **click on links for further information on how satellite imagery works** so that **I can further my understanding**
- 5.9 As a **New/returning Site User** I can **read about common applications of satellite imagery** so that **I have more understanding of the real life applications of the website**

### User Story 6
As a **Site User** I can **calculate the probability of my pipeline** so that **I can see what the chances are of successful results, and change my parameters if required**

- 6.1: As a **Site User** I can **view the probability of each interval returning an image** so that **I can see the percentage chance of receiving an image**
- 6.2: As a **Site User** I can **view the reason as to why the probability percentage is low** so that **I know which parameters I could change to attempt to increase the probability percentage**
- 6.3: As a **Site User** I can **return back to previous form tabs and adjust my parameters** so that **I can attempt to increase the chance of probability**
- 6.4: As a **Site User** I can **re-calculate the probability percentage** so that **I can understand how my form changes have changed the probability percentage**

User Story 6 was not implemented in the final deployed project, and was therefore not tested.

The Skywatch API allows users to [calculate the probability](https://api-docs.skywatch.co/#tag/pipelinePost) (%) that each interval will return an image.  This is based on the API's algorithm which will match up the AOI with a suitable satellite, as well as meteorology reports.  For example, an interval may only have a 40% chance of returning an image because there is excessive cloud cover forecast that day.  The user can then adjust their interval settings or cloud cover parameters to attempt to increase this percentage.

In a testing environment this feature was set up with a Javascript async *fetch* function to call the API with the user's chosen parameters, and the resulting probability numbers displayed on the Review page of the Create a Pipeline form.  The user could scroll back through the form tabs to adjust their form field values, and the probability would then re-calculate for the new parameters.  These probability percentage figures would not be stored in a model.

While the function worked as expected in the testing environment, the feature was not included in the final deployed project due to time restraints.  The User Story was a 'could-have' issue, and omitting this feature does not hamper the user's experience on the website.


### User Story 7
As a **Site User** I can **save an incomplete form** so that **I can return to the form in the future for committing**

- 7.1: As a **Site User** I can **save an incomplete form** so that **I can keep the parameters saved without having to commit**
- 7.2: As a **Site User** I can **see my saved pipelines on my My Pipelines page** so that **I know how many forms I have part-completed and are still to be completed**
- 7.3: As a **Site User** I can **click on one of my saved pipelines** so that **I can return to the incomplete form and continue working on it**
- 7.4: As a **Site User** I see **my saved pipeline parameters filled in on the Create a Pipeline form** so that **I don't have to input these again**

User Story 7 was not implemented in the final deployed project, and was therefore not tested.

An additional button could be added to the form on all tabs which would save the object, but not submit the pipeline parameters to the API.  The object would appear on the My Pipelines page under a new status category 'Saved Pipelines'.  When opened, the form would open with form fields filled in with any information the user had already input.

This feature could be implemented easily on another iteration of the project. While this feature may be beneficial, especially as the form is relatively long, it is not a feature which affects the overall functionality of the website.

### User Story 8
As a **Website Owner/Admin** I can **lock/restrict specific parameters in the admin panel** so that **for certain users I can control the details of the pipelines they submit**

User Story 8 was not implemented in the final deployed project, and was therefore not tested. 

The purpose of this feature was to allow the admin panel to restrict certain parameters for users.  For example, the admin could determine that one user could only access AOIs of 5,000 km2 as opposed to 10,000 km2.  

It became more evident throughout the development of the project that this feature would only be beneficial for purchased imagery, and adding restrictions for free data would further reduce the probability of the user receiving images for their pipelines. The developer felt it was more beneficial to allow users full scope of the free API data.

### User Story 9
As a **Site User** I can **see a visual graph of the progress of the pipeline** so that **I have a more visually pleasing understanding of the pipeline progress** (active pipelines only)

- 9.1: As a **Site User** I can **see a timeline spanning the full duration of my pipeline** so that **I can see when the pipeline starts and ends**
- 9.2: As a **Site User** I can **see a legend on the timeline** so that **I know what all icons and colours represent**
- 9.3: As a **Site User** I can **see all intervals in my pipeline** so that **I know when the intervals start, end, and the duration**
- 9.4: As a **Site User** I can **see the status of all pipelines colour-coded** so that **I can see which intervals have been completed, and which are still to be completed**
- 9.5: As a **Site User** I can **see today represented on the timeline** so that **I can gauge an understanding of how much of the pipeline has been completed, and how much is left**
- 9.6: As a **Site User** I can **see when images were delivered** so that **I know which intervals were successful**

### User Story 10
As a **Site User** I can **select the AOI for my pipeline on a map feature** so that **there is a more accessible way of selection/viewing my chosen AOI**

- 10.1: As a **Site User** I am **instructed to select an area of an interactive map** so that **my pipeline will retrieve satellite images of that area**
- 10.2: As a **Site User** I am **made aware of the restrictions of the map selection** so that **I can draw an area which will meet those restrictions**
- 10.3: As a **Site User** I am **given inline feedback of my map selection size** so that **I can adjust the area I drew if it does not meet the requirements**
- 10.4: As a **Site User** I am **given instructions on how to use the map features** so that **understand how to draw, select, edit and delete the area I drew**
- 10.5: As a **Site User** I can **zoom in and out on the map** so that **I can more easily find the area on Earth I am looking for**
- 10.6: As a **Site User** I am **given a review of the AOI I selected in the form review and my pipeline detail view** so that **I am reminded of the location of the AOI I selected**
- 10.7: As a **Site User** I can **see the geoJSON data/coordinates of the area I selected** so that **I can use this information in post production**

### User Story 11
As a **Site User** I can **view/download images and metadata of retrieved API results** so that **I can use this information in post production**

- 11.1: As a **Site User** I can **view a preview of a delivered image** so that **I can determine if the image is of good quality**
- 11.2: As a **Site User** I can **download the full-size image** so that **I can use the image for the purpose I need it/view it in higher resolution**
- 11.3: As a **Site User** I can **see the size of the full-size image** so that **I am aware how large in computer memory the image is**
- 11.4: As a **Site User** I can **see technical data associated with any delivered images** so that **I can determine if the image is of use to me/meets the parameters I set**
- 11.5: As a **Site User** I can **open a file containing the metadata associated with delivered images** so that **I can view further technical information about the image/satellite which took the image**

### User Story 12
As a **Site User** I can **edit details of my pipelines**

- 12.1: As a **New/returning Site User** I can **access the edit form on the pipeline detail page** so that **I can edit the pipeline**
- 12.2: As a **New/returning Site User** I can **see which parameters I can change for my pipeline** so that **I am aware of the limitations once my pipeline has been submitted**
- 12.3: As a **New/returning Site User** I can **change the name and description of my pipeline** so that **I can correct if needed, or add details about results in the description**
- 12.4: As a **New/returning Site User** I can **see if my pipeline is able to be edited** so that **I am aware if I can edit the pipeline and, if not, the reason why**
- 12.5: As a **New/returning Site User** I am **redirected back to the detail view of the pipeline** so that **I can see the changes I made reflected**
- 12.6: As a **New/returning Site User** I am **shown a timestamp of when the pipeline was last edited** so that **I am aware if and when I last edited my pipeline**

### User Story 13
As a **Site User** I can **delete my pipeline** so that **I can remove pipelines I no longer need, or were incorrect**

- 13.1: As a **Site User** I can **see the Delete Pipeline button on my pipeline view** so that **I can access the delete form**
- 13.2: As a **Site User** I am **provided with an intermediate view of deleting the pipeline** so that **I do not delete my pipeline immediately by pressing the Delete Pipeline button**
- 13.3: As a **Site User** I am **aware which pipeline I am about to delete** so that **I am certain which pipeline I am about to delete**
- 13.4: As a **Site User** I can **see a list of results of deleting the pipeline** so that **I am aware of the consequences of deleting a pipeline**
- 13.5: As a **Site User** I can **see an exit button when deleting my pipeline** so that **I can change my mind if I no longer want to delete this pipeline**
- 13.6: As a **Site User** I am **given feedback that the pipeline was deleted** so that **I have confirmation that the pipeline was deleted**

### Admin Goals
The Django admin panel can be used to view all pipelines and respective results, and pipelines can also be deleted from here. 

![Admin panel](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1644657234/adminlist_cifest.jpg)

![Admin list view](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1644657234/admindetail_n3izek.jpg)

![Admin result view](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1644657234/adminresult_y31nze.jpg)

[Back to top](#spaceport)

# Features
The section provides an overview of all features found in the website. 

## Homepage
## Products
## Product Detail
## Bag
## Checkout
## Checkout Confirmation
## Profile
## Liked Products
## Add Product (admin)
## Edit Product (admin)
## Copy/duplicate Product (admin)
## Error Pages
## Notifications
## Sign Up
## Sign In
## Log Out


# Technologies Used

## HTML/CSS
The project uses [HTML](https://en.wikipedia.org/wiki/HTML) language to build the website pages.
[CSS](https://en.wikipedia.org/wiki/CSS) is used to style the pages.

## Javascript
[Javascript](https://www.javascript.com/) is included on most pages.  The main functions are:


## Python
[Python]((https://www.python.org/)) was used for server side coding on the project.

## Django
- [Django](https://www.djangoproject.com/) is the framework used in this project
- The Django templating language was used to render pages
- The Django [unit test library](https://docs.djangoproject.com/en/3.2/topics/testing/overview/) was used for unit tests
- The Django allauth library was used for user authentication.

## APIs
Two APIs were implemented into the project.

## Other Libraries
- Bootstrap 5.0 (https://getbootstrap.com/docs/5.0)
The project uses the bootstrap library for some UI components in the website (Buttons, Card, Carousel, Modal, Pagination, Navbar),
- Postgres (https://www.postgresql.org/)
The deployed project on Heroku uses a Postgres database,
- Gitpod (https://gitpod.io/)
Gitpod was used as an IDE for the project.
- Github (https://github.com/)
GitHub was used to store the project code in a repository
- Balsamiq (https://balsamiq.com/)
Balsamiq was used to create the website wireframes.
- Chrome dev tools (https://developers.google.com/web/tools/chrome-devtools)
For troubleshooting and debugging of the project code
- Responsive Design (http://ami.responsivedesign.is/)
Website for generating the responsive image in this README
- Python Online Editor (https://www.online-python.com/)
This software was found useful to perform code without having to, for example, create a new form every time the developer wanted to change something
- JS Beautifier (https://jsonformatter.org/jsbeautifier)
This was used frequently to copy in large JSON files from the API to view the contents
- Font Awesome (https://fontawesome.com/)
Font awesome was used to provide the relevant fonts/icons for the website

[Back to top](#spaceport)

# Testing
The testing strategy is detailed in [this document](TESTING.md).

# Additional Features
This section details some additional features which could be added to further develop the website.



[Back to top](#spaceport)

# Deployment
### Local Deployment
To run this project locally, you will need to clone the repository.  You will also need a Skywatch API key, and a Mapbox Access Token. 

#### Mapbox Access Token
1. Navigate to [Mapbox](https://www.mapbox.com/)
2. Create an account with Mapbox.
3. Navigate to your account page and click 'Create a Token' and create a Public Token

![Mapbox create token](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1644512336/mapboxacces_rgirat.jpg)
![Mapbox public key](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1644512336/mapboxaccesstoken_jefps0.jpg)

#### Skywatch API Key
Create an API key with Skywatch will require navigating to the [Request Access](https://www.skywatch.com/earthcache/get-access) webpage and then awaiting approval.  If there are any issues with requesting access, the developer can provide their own API key, but it is *really important* that this is only used for the purposes of testing the project locally, and that 'max_cost' in the 'create' view is kept to zero.

#### Cloning Workspace
1. Log in to [Github](https://github.com/)
2. Select the repository MojosBeans100/ms4-spaceport
3. Click the Code button and copy the HTTPS url, for example: https://github.com/MojosBeans100/ms4-spaceport.git
4. In your IDE, open a terminal and run the git clone command, for example

<code>git clone https://github.com/MojosBeans100/ms4-spaceport.git</code>

The repository will now be cloned to your workspace.

5. Create an env.py file (do not commit this file to source control) in the root folder in your project, and add in the following code with the relevant key, value pairs, and ensure you enter the correct key values

<code>import os

os.environ.setdefault('SKYWATCH_KEY', TO BE ADDED BY USER)

os.environ.setdefault('MAPBOX_KEY', TO BE ADDED BY USER')</code>

6. Install the relevant packages as per the requirements.txt file
7. In the settings.py ensure the connection is set to either the Heroku postgres database or the local sqllite database
8. Add localhost/127.0.0.1 to the ALLOWED_HOSTS variable in settings.py
9. Run "python3 manage.py showmigrations" to check the status of the migrations
10. Run "python3 manage.py migrate" to migrate the database
11. Run "python3 manage.py createsuperuser" to create a super/admin user
12. Start the application by running python3 manage.py runserver
13. Open the application in a web browser, for example: http://127.0.0.1:8000/

### Heroku Deployment
To deploy this application to Heroku, run the following steps.

1. Create an account at [heroku.com](https://id.heroku.com/)
2. Create an app, give it a name - for example ms4spaceport - and select a region
3. Under resources search for postgres, and add a Postgres database to the app
4. Note the DATABASE_URL, this can be set as an environment variable in Heroku and your local deployment (env.py)
5. Install the plugins dj-database-url and psycopg2-binary
6. Run pip3 freeze > requirements.txt so both are added to the requirements.txt file
7. Create a Procfile with the text: web: gunicorn ms4spaceport.wsgi:application for example
8. In the settings.py ensure the connection is to the Heroku postgres database
9. Ensure debug is set to false in the settings.py file
10. Add localhost/127.0.0.1, and ms4spaceport.herokuapp.com to the ALLOWED_HOSTS variable in settings.py
11. Run "python3 manage.py showmigrations" to check the status of the migrations
12. Run "python3 manage.py migrate" to migrate the database
13. Run "python3 manage.py createsuperuser" to create a super/admin user
14. Install gunicorn and add it to the requirements.tx file using the command pip3 freeze > requirements.txt
15. From the CLI login to Heroku using the command heroku git:remote -a ms4spaceport
16. Disable collectstatic in Heroku before any code is pushed using the command heroku config:set DISABLE_COLLECTSTATIC=1 -a ms4spaceport
17. Push the code to Heroku using the command git push heroku master
18. Ensure the following environment variables are set in Heroku

![Heroku Config Vars](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1644513398/herokuconfigvars_vfhl5s.jpg)

19. Connect the app to GitHub, and in Manual Deploy, click deploy branch.

![Heroku Deploy Branch](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1644513541/heokudeploy_eaqdqh.jpg)

20. Click on the link provided to access the application
21. If you encounter any issues accessing the build logs is a good way to troubleshoot the issue

# Limitations
## Products
To build up an adequate database of products, a number of sources were used to provide images and descriptions for the products. The Products model contains a number of URLFields which credit these sources, and all images contain either an 'alt' or 'title' attribute which contains a link to source or owner of the image.

# Media
Images used on the site were sourced from the following sources.  Images which are free to use publicy were desirable, however when this was not possible the images are credited.

- Pexels
    - SpaceX
    - Pixabay
- GettyImages
- Spectator Earth
- Nasa Earth Observatory
- NOAA GOES Geostationary Satellite
- Science Friday
- Discover Magazine
- https://www.nknews.org
- Axios
- Mapbox
- Terraprints
- Maxar
- ABC
- New York Latest
- BBC News
- Working on Cruise Ships
- Skywatch
- Fine Art America
- Farmonaut

# Credits

Images as acknowledged above
- [Font Awesome](https://fontawesome.com/) for us of icons
- [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/) documentation for information about how to style the HTML 
- [W3 Schools](https://www.w3schools.com/) for use of tabbed form and jump to top button
- [Mapbox](https://www.mapbox.com/) for use of the map feature in Create Pipeline form and detail view
- [ChartJS 3.7.0](https://www.chartjs.org/docs/latest/) for creation of pipeline timeline
- [Skywatch](https://www.skywatch.com/) for use of their API
- [Django 4.0](https://docs.djangoproject.com/en/4.0/) documentation for information about the framework and template syntax
- [Stack Overflow](https://stackoverflow.com/) for help on a number of programming issues
- [geoJSON.io](http://geojson.io/#map=2/20.0/0.0) for selecting an AOI and getting a geoJSON output before the map feature was introduced
- [Patch Plants](https://www.patchplants.com/gb/en/) for website inspiration
- [Am I Responsive](http://ami.responsivedesign.is/) to create the banner image for this ReadMe


# Acknowledgements

I'd like to thank my mentor, Mo Shami, for providing me support throughout the development of this project.

I'd like to thank Paul (Github 'pmeeny'), for the inspiration for a great (although somewhat intimidating!) Readme format to follow.

I'd like to thank tutor support at Code Institute for many hours of technical help.

I'd like to thank Astrosat Ltd, who proposed the project idea and worked with Skywatch to get me access to their API.

I'd like to thank my family for taking time to use my project website and providing me helpful feedback. 