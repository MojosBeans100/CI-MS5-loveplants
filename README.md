# Love Plants
Love Plants is a Full Stack B2C (business to customer) e-commerce website which allows customers to view and purchase products related to plants. The website was developed for Milestone 5 as part of the Code Institute Diploma in Software Development. 

![Responsive website](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652351332/LovePlants/amirespoinve2_ibxytq.jpg)

# Table of contents
- [Project Overview](#project-overview)
- [UX](#ux)
  - [Strategy](#strategy)
  - [Scope](#scope)
  - [Structure](#structure)
  - [Skeleton](#skeleton)
  - [Surface](#surface)
- [Database](#database)
  - [Database Structure](#database-structure)
  - [Models](#models)
- [Features](#features)
  - [Homepage](#homepage)
  - [Products](#products)
  - [Product Detail](#product-detail)
  - [Bag](#bag)
  - [Checkout](#checkout)
  - [Checkout Confirmation](#checkout-confirmation)
  - [Profile](#profile)
  - [Liked Products](#liked-products)
  - [Add Product (admin)](#add-product-admin)
  - [Edit Product (admin)](#edit-product-admin)
  - [Create Sale (admin)](#create-sale-admin)
  - [Error Pages](#error-pages)
  - [Notifications](#notifications)
  - [Account Authentication](#account-authentication)
  - [T&Cs, Policy, FAQ](#tcs-policy-faq)
- [Technologies Used](#technologies-used)
  - [HTML/CSS](#htmlcss)
  - [Javascript](#javascript)
  - [Python](#python)
  - [Django](#django)
  - [Other Libraries](#other-libraries)
- [Testing](#testing)
- [Search Engine Optimisation (SEO)](#search-engine-optimisation-seo)
  - [Site content](#site-content)
  - [Keywords](#keywords)
  - [Images](#images)
  - [Responsiveness](#responsiveness)
  - [Links to useful pages](#links-to-useful-pages)
  - [Links to Social Media](#links-to-social-media)
  - [Expertise, Authoritativeness, Trustworthiness](#expertise-authoritativeness-trustworthiness)
  - [Sitemap.xml](#sitemapxml)
  - [Robots.txt](#robotstxt)
  - [Further Steps](#further-steps)
- [Marketing](#marketing)
  - [Further Marketing Strategies](#further-marketing-strategies)
- [Deployment](#deployment)
- [Limitations](#limitations)
  - [Products](#products)
  - [Description/ Care Instructions](#description-care-instructions)
- [Unfixed Bugs](#unfixed-bugs)
  - [Product Images](#product-images)
  - [Faceted Filtering](#faceted-filtering)
  - [Like Product](#like-product)
- [Media](#media)
  - [Images](#images)
- [Credits](#credits)
  - [Technologies](#technologies)
  - [Media](#media)
  - [Design](#design)
  - [Editors](#editors)
  - [Content](#content)
  - [Generators](#generators)
  - [SEO](#seo)
  - [Validators](#validators)
  - [Marketing](#marketing)
- [Acknowledgements](#acknowledgements)

# Project Overview
- This website was developed for submission as the Milestone 5 project of the Code Institute Diploma in Software Development.
- The website is deployed using the Heroku pages at the following url: https://ms5loveplants.herokuapp.com/
- The repository on Github that contains the website source code and assets is available at the following url: https://github.com/MojosBeans100/CI-MS5-loveplants
- The website was built with a responsive look and feel, designed to be enjoyable to use on all screen sizes. 

[Back to top](#love-plants)

# UX
The Five Planes method - strategy, scope, structure, skeleton, and surface - was used during the project planning phase to provide a conceptual framework for designing this e-commerce website.  The methodology for each plane is provided below. 

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
- To view and moderate customer ratings and reviews

### User Stories
All user stories are detailed in [this document](USER_STORIES.md), and in the [Issues](https://github.com/MojosBeans100/CI-MS5-loveplants/issues) subfolder in the Github repository for the project.

[Back to top](#love-plants)

## Scope
The Scope plane determines the scope of the project \
User Stories/Issues were mapped to Sprints (or Milestones) to plan for the current and next phase of the project. In general the Sprints were no longer than 2 weeks, and overall followed an organic order to developing an e-commerce website. 
The first sprints contained the higher priority features, providing basic website functionality to meet the project requirements (eg, allow users to checkout items).  The later sprints contained features which were not considered necessary but enhanced the project (eg, allow users to like and review products).

### Sprints
- Sprint 1 - basic project set up: user authentication, create models, homepage templates, display products
- Sprint 2 - the 'Bag' and 'Checkout' apps: add, edit, delete products in bag and checkout the order
- Sprint 3 - the 'Profile' app: provides users more detail about their profile, order history, review products.  Admin control of site.

### Epics, User Stories, Tasks
Epics were defined based on the main functions the website was expected to have, which mostly revolved around the main CRUD functions of the database. These Epics were refined into smaller User Stories, which could then be broken down into manageable tasks for the developer to complete within the current project iteration. User acceptance criteria was determined for each Epic/User Story

### Priority
Priority labels were assigned to each User Story/Issue, in order to determine which tasks to complete first in a Sprint. When the Issue was not completed, it could be included on another Sprint in order to complete it. Some User Stories were not completed.

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

- the **Love Plants logo** is kept to the top left of the page, irregardless of the screen size
- the main **navigation menu** is placed at the top of the page, and provides only a limited selection of options so as not to overwhelm the user
- the **footer** is kept fixed to the bottom of the screen, and contains contact information and useful links
- **anchor links** are styled with an underline feature on hover
- buttons represent important calls to action, such as submitting a form and maintain consistent colours as described [above](#consistency)
- as in most e-commerce sites, the top right of the page contains links to the **user's profile, bag, and log in/log out facilities**

#### Learnability
See below some examples of how the developer considered UX learnability when presenting the Love Plants brand, to help users achieve their goals quickly and efficiently

- use of **visuals**  as much as possible, such as icons to represent actions as opposed to text

Users see a heart icon to 'like' a product:
![Icon for liking product](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652345634/LovePlants/goodcontrast_mrjohi.jpg)

- **simplicity** in design, in effect minimising text, actions, colours.  The develop aims to only provide relevant information for the section or page, so as not cognitively overload the user with unnecessary information

Checkout page with 1 call to action:
![eg the checkout page provides only 1 CTA](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651590180/LovePlants/Testing/US%204/4.3/tablet2_upmyn0.jpg)

- **predictable process** regarding e-commerce websites, ie look for products > select a product > add product to basket > checkout

- **prioritising primary actions**, by providing the main call to action as a button, therefore more visual to users, even though there may be other links or actions on that page.  For example, on the bag, users can link back to other pages, but the priority action for that page is to checkout.

![checkout button](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651489084/LovePlants/Testing/US%203/3.5/desktop1_yaotvt.jpg)

#### Visibility
Decent UX/UI visibility is achieved on the website by providing obvious prompts and cues, and ensuring users are aware of all opportunities, for example:

- the navbar remains fixed to the top of the page, providing the user to opportunity to navigate to all high order pages, such as the Store (products) and their bag items
- users can obtain free delivery with a minimum basket total, ie by purchasing more products, and can see products which would increase their basket to this total
- users can see the opportunity to 'like' products, with the heart icon in the nav bar and on product cards

#### Feedback
As users have significant interaction with the site, feedback on their actions was considered important.  This was provided by:

- **in-line feedback** on forms, to emphasise invalid fields
- **notifications** on notable actions, such as adding a product to their basket.  This was achieved with Bootstrap 'toasts'
- **possible actions** available to them, namely to navigate around the site

[Back to top](#love-plants)

### Information Architecture
Information Architecture, or IA, was considered when creating the structure of the website, to allow users to understand where the information they want is in relation to their current position, and to deliver the right information at the right time.  Additionally:

- the **MVC architecture pattern** provided by Django allows the website to collect, manipulate and deliver the data

- a **database schema** was used to design the database models, and to understand how they communicate with one another. (See further information on the [database](#database))

- **content inventory** was provided by the in-built Django Admin panel, to maintain a database of products.  This is effectively mirrored in the front-end, with a more user-friendly option for the admin to, for example, create a product

[Back to top](#love-plants)

## Skeleton
The Skeleton plane defines the form, presentation, and arrangement of components defined in the Structure. 

### Interface Design
Initial wireframes were designed during the project proposal stage to mock-up the main website pages (ie homepage, products, product detail, checkout etc).  During development, these designs evolved to better suit the website content, but provided the developer a framework to work from when designing the front-end.  

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

### Navigation Design
Navigation design was considered based on the main functions of the website. A typical user wishes to:

- determine the purpose of the site, and what kind of products to expect (users are directed to the homepage intially)
- view all available products (users can access the products page directly through the nav bar, or via the calls to action on the homepage)
- narrow their search down to one or a few products (users can choose products they wish to view on the products page and are directed to the product detail page)
- view the items they have in their bag (once added, the notification presents the user their bag, also accessible via the bag icon in the nav bar)
- buy their items (from their bag there is an evident link to checkout)
- view confirmation that their purchase has been successful (once purchased, users are directed to the checkout confirmation)

This organic process for typical e-commerce site users was kept in mind when determining the layout of pages, content and available calls to action.

[Back to top](#love-plants)

## Surface
The look and feel of the website was considered when designing the visual elements of the product, to produce a polished product which brings together all other UX planes. Love Plants wishes users to choose their store over another store, thus visual design was an important aspect of the UX strategy. 

### Visual Design
Some aspects of visual design considered when developing Love Plants are detailed below. 

#### Alignment
In general, text is aligned left to support our natural reading pattern of left-to-right.  

Product cards align text left:
![Product card](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652300219/LovePlants/alignment_oyt7cu.jpg)

#### Repetition
Buttons maintain the same style and text throughout the site, with either white-on-black or black-on-white depending on the background.

![Button 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652300398/LovePlants/black_u5o148.jpg)
![Button 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652300397/LovePlants/button_hfiqzy.jpg)

#### Contrast and Colour
Contrast is used effectively on the website, as colours are minimised to white, black, and colour from product images. 
Text is clearly readable on all pages, and products are a welcomed splash of colour amidst an otherwise monochrome webpage. 

#### Consistency
Consistency is maintained through all elements.  One example of this is the layout of the page content.  On all pages, aside from the homepage, content is in a centered container which responds to the screen size (on smaller screens the container fills the screen, on larger screens there is padding around the container).  The user knows where to expect to see content when navigating to another page. 

#### Typography
Love Plants uses a different font to the standard Times New Roman, Arial, or native Bootstrap font.  The Raleway font was chosen because it is pleasant with an almost 'handwriting' effect, but maintains readability. 

[Back to top](#love-plants)

# Database

## Database Structure
The database includes:
- Home app
- Products app
- Profile app
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
- sitemap.xml, to provide search engines will available pages to browse
- robots.txt, to tell search engines where not to browse

[Back to top](#love-plants)

## Models
The models created to develop this e-commerce project are defined in this section. 

![database schema](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651259312/LovePlants/QuickDBD-export_wuephp.png)

### User (Django context processor)
- The User model contains information about the user, as part of the [Django allauth library](https://django-allauth.readthedocs.io/en/latest/installation.html)
- No additional features are added to this model, as a basic username, email and password satisfy the requirements of the project

### Home App
The Home App serves to display the homepage for the website.  
It contains no models. 

### Profiles App
(User Stories XXX)
The Profiles App provides the user the ability to create their website profile, so they can purchase products and review their details and order history. 

#### UserProfile
- The UserProfile model allows users to hold their personal information when using the site, and has a One-To-One relationship with the [User](#user-django-context-processor) model.
- The UserProfile model will be modified automatically upon the User model being modified

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
- The Products App serves to hold a database of products available to purchase, details about them, their categories and any reviews/ratings
- It contains 5 models (Product, ProductReview, Category, PlantCategory, RecentlyViewed)

#### Product
- The Product model holds information about specific products
- It has a model method (update_average_rating) to automatically update the average rating when a new ProductReview object is created

| Field | Description | Field type|
|-------|-------------|-----------|
|id|primary key (Django auto created|Primary Key|
|plant_category|plant category|CharField|
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
|sale_price|sale price of product|DecimalField|
|stock_quantity|quantity of the product in stock|PositiveIntegerField|
|pot_size|diameter of the pot|PositiveIntegerField|
|height|height of the product|PositiveIntegerField|
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
|live_on_site|whether or not the product is live on the website to be purchased|BooleanField|

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

[Back to top](#love-plants)

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
- The OrderLineItem model represents details about each product in any given order (Order model).
- The model contains a model method to update the lineitem_total if the quantity is changed.

| Field | Description | Field type|
|-------|-------------|-----------|
|order|the order this line item is in reference to|ForeignKey (Order)|
|product|the product on the order|ForeignKey (Product)|
|quantity|the quantity of this item on the order|IntegerField|
|lineitem_total|the total cost of this line item|DecimalField|

[Back to top](#love-plants)

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

[Back to top](#love-plants)

# Features
The section provides an overview of all features found in the website. 

## Homepage

## Products
The products page displays products available to purchase on the website.  

### Filter Products
(User Story 2.3)
This section provides faceted searching to narrow down product searches.  Users can filter by the plant type, price ranges, sunlight/watering required, whether or not the product is rare, popular, low maintenace, whether they have 'liked' the product.

![Faceted searching](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652124839/LovePlants/ReadMe/productsfilter_dzmst1.jpg)

### Sort Products
(User Story 2.4)
Users can also sort the products by price (low, high), rating (low, high) and name (alphabetically).

![Sorting](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652124838/LovePlants/ReadMe/productsort_mcumam.jpg)

### Product List
(User Story 2.1)
A list of products which match the filter and search criteria are displayed throughout the rest of the page.  Products are displayed with:
- a Bootstrap card, providing an image of the product (which the second product image displayed upon hover of the original image).  The card links to the detailed view of the product when clicked
- the name of the plant
- the latin (or botanical) name
- the price
- the sale price (if relevant)  
- the 'like' button (rendered in black if the product is 'liked' by the user, white if not)

![Liked product](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652124839/LovePlants/ReadMe/productliked_kbluiw.jpg)
![Not liked product](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652124838/LovePlants/ReadMe/notliked_m5kit2.jpg)

[Back to top](#love-plants)

## Product Detail
The product detail page provides further information about the product in question.

### Breadcrumb Navigation
(User Story 2)
This feature allows for users to see which category the plant belongs to, and also allows users to navigate back to the products page by clicking on any of the links provided. Users can also use the browser 'back' button to return to the previous page, which would maintain their chosen filter and sort criteria. 

![Breadcrumb navigation](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652124838/LovePlants/ReadMe/breadcrumb_bqy2dr.jpg)

### Images
(User Story 2)
The main product image sits above three smaller images, any of which can be clicked for the user to view more images.  They decrease in opacity on hover so the user is aware they are clickable.

![Product images](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652124839/LovePlants/ReadMe/productimages_msfm5n.jpg)
![Product images 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652124839/LovePlants/ReadMe/productimage2_txhnuo.jpg)

### Additional Details
(User Story 2.5)
Further details about the product are provided for the user to learn more about the product.  The information includes:
- the pot size
- the height or length of the plant
- the maturity of the plant
- the sunlight and watering requirements
- the care maintenance
- a description of the product
- further care instructions
- the average rating, based on user reviews

![Product details](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652124839/LovePlants/ReadMe/productdetail_rfhvws.jpg)

[Back to top](#love-plants)

### Reviews
(User Story 5)
If any reviews have been left by users for the product, they are displayed in a set of rows beneath the care instructions.  Users can see the average rating, how many reviews have been given, comments written by users, and how long ago they were left. 

![User reviews](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652124838/LovePlants/ReadMe/reviews_mrclcx.jpg)

### Review Form
(User Story 5)
If a user has purchased the product, and not previously left a review, they can leave a comment and provide a rating from 1 to 5 in a short form. 

![Review form](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652124985/LovePlants/ReadMe/reviewform_ifwvnm.jpg)

### Suggested Products
(User Story 2.7)
To keep the user interested in browsing products, suggestions are made for additional products to view.  The list is kept brief, to only 4 products per category, and products are not duplicated between lists.  The categories are:
- rare products (if the product is rare)
- popular products (if the product is popular)
- easy care products (if the product has low care maintenance)

![Suggested products](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652125041/LovePlants/ReadMe/additionaprodcts_xde83c.jpg)

### Add To Bag
(User Story 3.1)
Users can add the product in question to their bag, by selecting the desired quantity and clicking 'Add to bag'.  The page does not redirect, but provides a notification for users to see if the action has been successful.  This section includes the price, or sale price, of the product. 

![Add to bag](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652125077/LovePlants/ReadMe/addtobag_igtcac.jpg)

[Back to top](#love-plants)

## Bag
The Bag page displays the contents of a user's bag and a link to checkout.

### Product List
(User Story 3.2, 3.4)
Identifying details are displayed for each product, namely the plant name, price or sale price, subtotal, quantity and pot size.  Users can click on either the image or the product name to redirect to the product detail page. Users can also 'like' or 'unlike' the product on this page. Users can adjust the product quantity in the bag, or remove it from the bag completely.  

![Product list](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652125323/LovePlants/ReadMe/bagproducts_a0fblh.jpg)

### Free Delivery
(User Story 3.4)
Users are aware how much they would need to spend on top of what is already in their bag to qualify for free delivery.  Below the bag, a list of suggested products to reach this total are displayed, organised by lowest cost. 

For example if the user would need to spend £8.02 further to qualify for free delivery, products more expensive than £8.02 are listed, organised by cheapest first. These products have a 'Quick Add' button to prevent the need for the user to visit the product detail page to add to the bag. 

![Free delivery products](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652125323/LovePlants/ReadMe/freedelivery_kepmhh.jpg)

### Price Breakdown
(User Story 3.3)
The bag total, delivery cost and grand total are listed, as well as a link to checkout the bag. 

![Price breakdown](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652125323/LovePlants/ReadMe/pricebreakdown_smeglw.jpg)

### Suggested Products
(User Story 2.7)

Another list of suggested products are included on this page. This list is not organised or sorted by any particular criteria, and largely exists to encourage users to add more products.

![Suggested products](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652125323/LovePlants/ReadMe/suggestproducts_iuh13q.jpg)

[Back to top](#love-plants)

## Checkout
The checkout page requires users to input their delivery details and payment information.

### User Details
(User Story 4.1, 4.4)
Form fields are displayed for the user to input their personal and delivery information in order to process the order. Users can save their information for later, so the next order they submit will not require inputting this information again. 

![User details](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652125481/LovePlants/ReadMe/checkoutdetails_gv7xji.jpg)

### Bag Contents
(User Story 4.2)
Users are reminded of the contents in their bag on this page. Users can remove items from their basket on this page too. 

![Bag contents](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652125481/LovePlants/ReadMe/bagcontents_cgrukb.jpg)

### Order Summary
(User Story 4.3)
The same price breakdown from the bag page is displayed on this page. 

![Price breakdown](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652125481/LovePlants/ReadMe/ordersummary_yki8v9.jpg)

### Payment Section
(User Story 4.3)
Users are required to input their card details into the card payment section provided by Stripe, which shows validation if the card details are incorrect.  Users can click 'Secure Checkout' to complete the order. 

![Submit order](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652125481/LovePlants/ReadMe/customerservice_rtlicr.jpg)

### Form Submitted
(User Story 4.5)
Users have immediate feedback that their order is processing by displaying a 'loading' screen, which also prevents the user from clicking any other calls to action during order completion. 

![Submitted order](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651600558/LovePlants/Testing/US%204/4.5/desktop_yqyx3x.jpg)

[Back to top](#love-plants)

## Checkout Confirmation
(User Story 4.5)
The checkout confirmation/checkout success page displays details of the submitted order.  Users have confirmation it has been received.  All details about the order are provided for the user to verify.  There are no calls to action on this page.

![Checkout confirmation 1](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652125593/LovePlants/ReadMe/checkoutconfirm1_hdd4tp.jpg)

![Checkout confirmation 2](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652125593/LovePlants/ReadMe/checkoutconfirm2_ciusdm.jpg)

[Back to top](#love-plants)

## Profile
The profile page displays information about the user.

### Profile Details
(User Story 1.3)
Users can see information about their account settings, which also provide links to logging out and resetting their password.

![Profile details](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652360791/LovePlants/ReadMe/profile_zksong.jpg)

### Default Order Information
(User Story X)
Users can save default delivery information, which will auto-fill in on the checkout form for convenience. 

![Default delivery info](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652360791/LovePlants/ReadMe/profiledeafult_wctawh.jpg)

### Order History
(User Story 1.4)
Users can see a list of previous orders they have submitted, expanded each item to see further information.

![Order history](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652360791/LovePlants/ReadMe/profileorders_y33jzr.jpg)

[Back to top](#love-plants)

## Liked Products
(User Story 5.4)
This brief page display products the user has 'liked', and links to the product detail for each product. 

![Liked products](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652360791/LovePlants/ReadMe/liked_iyvnvp.jpg)

## Add Product (admin)
(User Story 6.2)
The Add Product page allows site administrators to add a new product on the website.  It contains a form to submit the details, and allows users to either add the product to the site or save it and return to it later. 

![Add product](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652361446/LovePlants/ReadMe/addproduct_qdxuue.jpg)

## Edit Product (admin)
(User Story 6.1, 6.4, 6.5)
Admin users can also edit the details of products, or delete the product.  This page also allows admin users to copy a product and save it as a new item. This is useful for products which are similar, for example a variegated species of another plant. 

![Edit product](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652361446/LovePlants/ReadMe/edit_procut_pidu9x.jpg)

## Create Sale (admin)
(User Story 6.3)
Admin users can put items on sale with this page.  They can apply a discount to all products or individual products, either by a percentage or a fixed amount.  They can also remove the sale price on this page, to revert products back to their original prices. 

![Create sale](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652361446/LovePlants/ReadMe/createsale_qumsqz.jpg)

[Back to top](#love-plants)

## Error Pages
(User Story 6.7)

A 404 error page is displayed if users attempt to access admin pages.

![404 page](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652005403/LovePlants/Testing/desktoperror_fvoibd.jpg)

## Notifications
(User Story 3.2, 3.3)

All users can see notifications in the form of Bootstrap 'toasts' to confirm an action has been completed.

![Notification](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651414942/LovePlants/Testing/US%203/3.1/desktop1_xtuvsa.jpg)

## Account Authentication
(User Story 1)

Users can sign up, log in, log out via the account authentication pages. 

![Sign Up Form](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652355766/LovePlants/Testing/US1/1.1/desktop3_j8qgvp.jpg)

## T&Cs, Policy, FAQ
Some generic e-commerce website pages are provided to enhance the professionalism of the website. 

![T&Cs](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652362047/LovePlants/ReadMe/T_Cs_rcvz5r.jpg)
![Policy](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652362046/LovePlants/ReadMe/policy_fhphdt.jpg)
![FAQ](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652362045/LovePlants/ReadMe/faq_upmp22.jpg)

# Technologies Used
## HTML/CSS
The project uses [HTML](https://en.wikipedia.org/wiki/HTML) language to build the website pages.
[CSS](https://en.wikipedia.org/wiki/CSS) is used to style the pages, along with [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/).

## Javascript
[Javascript](https://www.javascript.com/) is included on most pages.

## Python
[Python 3.8]((https://www.python.org/)) was used for server side coding on the project.

## Django
- [Django](https://www.djangoproject.com/) is the framework used in this project
- The Django templating language was used to render pages
- The Django [unit test library](https://docs.djangoproject.com/en/3.2/topics/testing/overview/) was used for unit tests
- The Django allauth library was used for user authentication.

## Other Libraries
- Bootstrap 5.0 (https://getbootstrap.com/docs/5.0)
The project uses the bootstrap library for some UI components in the website (Buttons, Card, Carousel, Modal, Pagination, Navbar)
- Postgres (https://www.postgresql.org/)
The deployed project on Heroku uses a Postgres database
- Gitpod (https://gitpod.io/)
Gitpod was used as an IDE for the project
- Github (https://github.com/)
GitHub was used to store the project code in a repository
- Balsamiq (https://balsamiq.com/)
Balsamiq was used to create the website wireframes
- Chrome dev tools (https://developers.google.com/web/tools/chrome-devtools)
For troubleshooting and debugging of the project code
- Responsive Design (http://ami.responsivedesign.is/)
Website for generating the responsive image in this README
- Python Online Editor (https://www.online-python.com/)
This software was found useful to perform code in a practice environment
- JS Beautifier (https://jsonformatter.org/jsbeautifier)
This was used to view large JSON files in a readable format, ie information from Stripe
- Font Awesome (https://fontawesome.com/)
Font awesome was used to provide the relevant fonts/icons for the website
- Flaticon Plant Images (https://www.flaticon.com/packs/indoor-plants-1)
Plant icons created by Icongeek26 were used in the products filter section 
- Google Fonts (https://fonts.google.com/)
For choosing a website font
- Markdown ToC Generator (https://luciopaiva.com/markdown-toc/)
For creating a Table of Contents for markdown files

[Back to top](#love-plants)

# Testing
The testing strategy is detailed in [this document](TESTING.md).

# Search Engine Optimisation (SEO)
The following Search Engine Optimisation techniques were employed on the website to improve audience reach.

## Site content
During development, it was ensured that the website is geared to the user needs, to make user experience better. 
The content is clear, uncluttered, and easy to navigate.  Users are clear of the purpose of the website, and the products contained in it. 

The UX development is detailed in [this section](#ux).

## Keywords

### Research
Thorough keyword research was undertaken, to determine words and phrases relevant to the product.  A brainstorm map of short-tail and long-tail keywords was produced, and optimised to remove items which Love Plants does not provide a solution to.

![Short tail keywords](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652163727/LovePlants/ReadMe/1_hga5zy.png)
![Long tail keywords](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652163727/LovePlants/ReadMe/2_oy4wkq.png)

### Optimisation
These lists of keywords could be optimised by determining which would be most effective on the website.  [Word Tracker](https://www.wordtracker.com/) was used to identify which words were deemed:

- high volume, low competition
- low volume, high competition

Word Tracker results for 'houseplant':
![Word tracker results](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652164429/LovePlants/ReadMe/keywords_houseplants_nz7q4k.jpg)

Word Tracker results for 'variegated plants':
![Word tracker results](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652164516/LovePlants/ReadMe/keyword_variegated_oyamnz.jpg)

Using these results, a brief study could be made to determine the most effective keywords to include on the website.  An example of one comparison made between two keyword phrases:

|Keyword(s)|Volume|Competition|
|----------|------|-----------|
|'indoor plants'|52,250|22.28|
|'indoor potted plants'|27,700|6.06|

The keyword 'indoor potted plants' was deemed more beneficial, as it had far lower competition compared to 'indoor plants', yet relatively high volume of web traffic.  Keywords which had a high volume but low competition were prioritised over keywords of low volume, high competition. 

The keyword research also gave insight into which houseplants were most popular - for example in the 'houseplants' Word Tracker results, the following plants have a high volume of searchers implying they are highly sought-after:
- snake plant
- peace lily
- spider plant
- philodendron
- prayer plant
- dracaena
- devil's cactus

These plants were included in the database of plants available to purchase, to attract customers to the website when searching for these products, and to further increase SEO metrics. 

### Implementation
These keywords were introduced into the website, maintaining an organic flow of content and avoiding 'keyword stuffing'.

#### Metadata
All relevant keywords were included in the metadata tag in the base.html file.

![Metadata](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652165361/LovePlants/ReadMe/metadta_okaby7.jpg)

#### Semantic Content
Keywords from the optimised lists were integrated into the website content where possible and relevant.  Keywords were used in semantic HTML elements, such as <code>h1</code>, <code>h2</code>, <code>span</code>, <code>strong</code> and <code>em</code> tags.

![Keywords in HTML content](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652165873/LovePlants/ReadMe/keywordsinhtml_udyof6.jpg)

## Images
While high quality images are sourced where possible, some improvements could be made to optimise images for SEO.  Images on an e-commerce website are desired to be high in quality, low in size, consistent in style, have descriptive names and always contain an <code>alt</code> tag for when the image does not load. 

### Optimizing Images for SEO
- This website uses Cloudinary as a cloud-based image storage system, which automatically generates links to insert into the 'src' attribute for <code>img</code> tags.  The product name is included in this link.  
- The <code>alt</code> tag for product images contains the product name and latin name, to ensure it is useful for determining the image content. 
- Many image <code>alt</code> or <code>title</code> tags include keywords.

### Improvements for Images for SEO
- Some of the product images have a 'squashed' appearance, due to the difficulties in sourcing images of the same height:width ratio. See [this section](#unfixed-bugs) for further information. 
- Images could be compressed to a smaller size, or a Webp file could be used rather than a .png or .jpeg, to improve website loading times. 

## Responsiveness
Quality of content is not compromised on smaller screens; the website is designed to be mobile and tablet friendly.  This is validated through extensive manual testing (see [Testing](TESTING.md#manual-testing)), and using [Google Mobile-Friendly Test](https://search.google.com/test/mobile-friendly) (see [Testing](TESTING.md#seo-testing)).

## Links to useful pages
Love Plants contains links to other high quality relevant websites, to further improve the website ranking.  While links to other online houseplant stores are not included in order to minimise competition, links to websites providing information about plant care, interesting articles and magazines are included in the website content. 

- The Spruce
- Gardener's World
- Gardening Know How

![Other websites](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652207674/LovePlants/othersources_kizp2l.jpg)

## Links to Social Media
In the footer, a link to the Love Plants Facebook page is provided for users to engage more with the store.  There are also icons for Instagram, Twitter and LinkedIn, although for the purposes of this project they do not provide a link to a page. 

## Expertise, Authoritativeness, Trustworthiness
The following criteria were followed to maintain a website providing expertise, authoritativeness and trustworthiness.

1. Understand users needs and create engaging content that meets the needs \
Website content was regarded as the most important criteria.  See [UX](#ux) for further information.

2. Maintain professional content, avoid typos and spelling mistakes \
The deployed project URL was input into [W3 Spellchecker](https://www.w3.org/2002/01/spellchecker), and aside from not recognising some plant latin/botanical names ie 'dracaena fragrans', and differences in American and British spelling (color/colour), there were no typographical errors. 

3. Answer user's questions in Frequently Asked Questions (FAQ) \
The 'Care' page provides users with further information about caring for their houseplants.
There is a separate 'FAQ' page with generic e-commerce application questions, which was copied from [Harper Collins](https://harpercollins.co.uk/pages/ecommerce-faqs) with minor adjustments to suit Love Plants. 

4. Ensure information is correct, provide citations and show research \
In this website, a lot of text content is sourced from other websites which have more expertise in terms of houseplants. Any content which was not written by the developer is cited by providing a reference to the webpage. 
For example, a lot of the plant descriptions and care instructions are sourced from [The Spruce](https://www.thespruce.com/houseplants-4127735). These are adequately credited by linking the document in the description.

![Citing sources](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652292218/LovePlants/citing_lpq0fk.jpg)

5. Add relevant links to other parts of the site to keep users exploring more content \
- Users are linked to the 'Care' page from the product detail page
- The website footer provides useful links to many pages in the site
- The homepage provides users with an instant product filter depending on what kind of product they are looking for ie. 'Rare plants', 'Popular plants', 'Easy care plants'

6. Providing links to Privacy Policy and T&Cs to convey trustworthiness to the user \
The following websites were used to generate generic documents.
[Terms and Conditions generator](https://www.termsandconditionsgenerator.com/) \
[Privacy Policy generator](https://www.privacypolicygenerator.info/)

7. Include testimonials, reviews, ratings \
Users may provide a review and rating to a product they have purchased, to allow for other users to trust the quality of the product, or understand its downfalls. 

8. Ensure quality of media is high \
In general, product images are of high quality and sized appropriately.  Limitations of this are outlined [here](#unfixed-bugs).

## Sitemap.xml
A sitemap.xml file was generated using [XML Sitemaps](https://www.xml-sitemaps.com/), whereby the deployed project link was inserted and a list of important URLs was retrieved.  This document speeds up content discovery when search engines are crawling the website, to ensure no important URLs are missed.

## Robots.txt
A robots.txt file was created to manage traffic to the website and tell a search engine where they are not allowed to go on the website, for example, the account authentication pages (Sign Up, Log In etc).
Having this files also shows acknowledgement that search engines are allowed on the site and have free access to it, which improves SEO quality.

## Further Steps
This section describes further steps which would be required to deploy the web application to a custom domain.  These steps were not carried out in this development project.

1. Register sitemap with Google
https://developers.google.com/search/docs/advanced/sitemaps/build-sitemap

2. Test robots.txt file
https://support.google.com/webmasters/answer/6062598?hl=en

3. Perform analytics study to determine:
- Click through rate - how ofter users click the Love Plants page link in Google search
- Bounce rate - how likely a user is to click the back button as soon as they land on Love Plants
- Dwell time - how long user stays on the Love Plants page before click back through search results
- Session time - how long user spend on Love Plants as a whole
- Pagers per session - how many pages users visited on Love Plants before moving on to another website

[Back to top](#love-plants)

# Marketing
The primary marketing techniques used for the Love Plants store were social media marketing (by linking a Facebook page) and email marketing (by providing an email sign-up for subscribing).

1. SEO \
The SEO strategies used for the development of this e-commerce store are documented [here](#search-engine-optimisation-seo)

2. Social media marketing \
Love Plants uses social media marketing to reach a wide range of customers.  
This marketing platform allows Love Plants to build the brand, connect and interact with potential and existing customers, share regular content and updates, and provide additional customer service and support. 

[Love Plants Facebook Page](https://www.facebook.com/loveplantsstore/)

![Screenshots from Facebook page](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652277509/LovePlants/fb1_x0l2bs.jpg)
![Screenshots from Facebook page](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652277509/LovePlants/fb4_vqveag.jpg)
![Screenshots from Facebook page](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652277509/LovePlants/fb3_ge8dpr.jpg)
![Screenshots from Facebook page](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652277509/LovePlants/fb2_hu25xu.jpg)

3. Email marketing \
Love Plants uses email marketing to reach customers who have subscribed to the mailing list.  As an e-commerce store, it is hugely advantageous to notify customers of flash sales, price drops, new stock and featured products in a quick and convenient manner. 

Love Plants users [Mailchimp](https://us18.admin.mailchimp.com/) to supply a 'Subscribe to Love Plants' form at the end of the homepage.  Users can enter an email address and will be notified when they have successfully joined the mailing list. 

![Subscribe Form](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652428221/LovePlants/signup_owjtoc.jpg)
![Subscribe Form](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652428220/LovePlants/signup3_ca4dlq.jpg)

## Further Marketing Strategies
The following marketing strategies were not used for Love Plants, but would be advantageous to include in a real e-commerce store. 

1. Content marketing \
Aside from creating useful, engaging content within the website, such as the Care page to advise users how to care after their houseplants, additional content marketing strategies - such as blog posts, videos and podcasts - were not implemented during the development of the project. 

2. Paid advertising
3. Influence marketing
4. Affiliate marketing
5. Paid social media marketing

[Back to top](#love-plants)

# Deployment

### Secret Keys
A couple of secret keys will need to be generated in order to run this project.

## Google emails
To set up the project to send emails and to use a Google account as an SMTP server, the following steps are required
1. Create an email account at google.com, login, navigate to Settings in your gmail account and then click on Other Google Account Settings
2. Turn on 2-step verification and follow the steps to enable
3. Click on app passwords, select Other as the app and give the password a name, for example Django
<br>![App password]()
4. Click create and a 16 digit password will be generated, note the password down
5. In the env.py file, create an environment variable called EMAIL_HOST_PASS with the 16 digit password
6. In the env.py file, create an environment variable called EMAIL_HOST_USER with the email address of the gmail account
7. Set and confirm the following values in the settings.py file to successfully send emails
<br><code>EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'</code>
<br><code>EMAIL_USE_TLS = True</code>
<br><code>EMAIL_PORT = 587</code>
<br><code>EMAIL_HOST = 'smtp.gmail.com'</code>
<br><code>EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')</code>
<br><code>EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASS')</code>
<br><code>DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_HOST_USER')</code>
8. You will also need to set the variables EMAIL_HOST_PASS and EMAIL_HOST_USER in your production instance, for example Heroku

## Stripe
1. Register for an account at stripe.com
2. Click on the Developers section of your account once logged in
3. Under Developers, click on the API keys section
<br>![API keys]()
4. Note the values for the publishable and secret keys
5. In your local environment(env.py) and heroku, create environment variables STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY with the publishable and secret key values
<br><code>os.environ.setdefault('STRIPE_PUBLIC_KEY', 'YOUR_VALUE_GOES_HERE')</code>
<br><code>os.environ.setdefault('STRIPE_SECRET_KEY', 'YOUR_VALUE_GOES_HERE')</code>
6. Back in the Developers section of your Stripe account click on Webhooks
7. Create a webhook with the url of your website <url>/checkout/wh/, for example: https://ms5loveplants.herokuapp.com/checkout/wh/
8. Select the payment_intent.payment_failed and payment_intent.succeeded as events to send
<br>![Webhook]()
9. Note the key created for this webhook
10. In your local environment(env.py) and heroku, create environment variable STRIPE_WH_SECRET with the secret values
<code>os.environ.setdefault('STRIPE_WH_SECRET', 'YOUR_VALUE_GOES_HERE')</code>
11. Test out the webhook and note the success/fail attempts for troubleshooting

### Local Deployment
To run this project locally, the repository will need to be cloned.  

#### Cloning Workspace
1. Log in to [Github](https://github.com/)
2. Select the repository MojosBeans100/CI-MS5-loveplants
3. Click the Code button and copy the HTTPS url, for example: https://github.com/MojosBeans100/CI-MS5-loveplants.git
4. In an IDE, open a terminal and run the git clone command, for example

<code>git clone https://github.com/MojosBeans100/CI-MS5-loveplants.git</code>

The repository will now be cloned to the workspace.

5. Create an env.py file (do not commit this file to source control) in the root folder in the project, and add in the following code with the relevant key, value pairs, and ensure you enter the correct key values

6. Install the relevant packages as per the requirements.txt file
7. In the settings.py ensure the connection is set to either the Heroku postgres database or the local sqlite database
8. Add localhost/127.0.0.1 to the ALLOWED_HOSTS variable in settings.py
9. Run "python3 manage.py showmigrations" to check the status of the migrations
10. Run "python3 manage.py migrate" to migrate the database
11. Run "python3 manage.py createsuperuser" to create a super/admin user
12. Start the application by running python3 manage.py runserver
13. Open the application in a web browser, for example: http://127.0.0.1:8000/

[Back to top](#love-plants)

### Heroku Deployment
To deploy this application to Heroku, run the following steps.

1. Create an account at [heroku.com](https://id.heroku.com/)
2. Create an app, give it a name - for example 'loveplants' - and select a region
3. Under resources search for postgres, and add a Postgres database to the app
4. Note the DATABASE_URL, this can be set as an environment variable in Heroku and the local deployment (env.py)
5. Install the plugins dj-database-url and psycopg2-binary
6. Run pip3 freeze > requirements.txt so both are added to the requirements.txt file
7. Create a Procfile with the text: web: gunicorn ms5loveplants.wsgi:application for example
8. In the settings.py ensure the connection is to the Heroku postgres database
9. Ensure debug is set to false in the settings.py file
10. Add localhost/127.0.0.1, and ms5loveplants.herokuapp.com to the ALLOWED_HOSTS variable in settings.py
11. Run "python3 manage.py showmigrations" to check the status of the migrations
12. Run "python3 manage.py migrate" to migrate the database
13. Run "python3 manage.py createsuperuser" to create a super/admin user
14. Install gunicorn and add it to the requirements.tx file using the command pip3 freeze > requirements.txt
15. From the CLI login to Heroku using the command heroku git:remote -a ms5loveplants
16. Disable collectstatic in Heroku before any code is pushed using the command heroku config:set DISABLE_COLLECTSTATIC=1 -a ms5loveplants
17. Push the code to Heroku using the command git push heroku master
18. Ensure the following environment variables are set in Heroku

![Heroku Config Vars](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1644513398/herokuconfigvars_vfhl5s.jpg)

19. Connect the app to GitHub, and in Manual Deploy, click deploy branch.

![Heroku Deploy Branch](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1644513541/heokudeploy_eaqdqh.jpg)

20. Click on the link provided to access the application
21. If any issues are encountered, accessing the build logs is a good way to troubleshoot the issue

[Back to top](#love-plants)

# Limitations
## Products
To build up an adequate database of products, a number of sources were used to provide images and descriptions for the products. The Products model contains a number of URLFields which credit these sources, and all images contain either an 'alt' or 'title' attribute which contains a link to source or owner of the image.  

In a true e-commerce store, these URL source fields would not be necessary, as all content is expected to be original. 

## Description/ Care Instructions
Upon research of other houseplant websites, it was noted that most included a brief paragraph description about the plant and some basic care instructions.  The developer saw the merit in including this information, and so included fields to represent these in the Product model.  

In a similar vein to the point above, while these were included in the model, these sections of text were sourced from other websites to reduce the time consuming task of writing these details for every product (furthermore, the developer would need to have extensive knowledge about botanicals to create this information).  The sources for these sections of text are attributed with a source and source url field in the model. On the product detail page, at the end of each section of text it provides an anchor link to the source itself, so there is no ambiguity as to where this information was sourced from. 

In reality, an e-commerce store would only include original information about the product. 

# Unfixed Bugs

## Product Images
As all images are sourced from 3rd party sites (all images are attributed to the source), they are downloaded with different width:height ratios.  As the developer felt the site appeared more attractive with all images of a constant size, for example, in the products page, some of the images appear 'squashed' and of lower quality due to being resized to the same size as all other images.  

The images are also highly varying in terms of the way the plant is style, presented, and the background colours and contents. 

While this is unfortunate, the developer felt it was important to build up a reasonable database of products and thus these images were deemed acceptable for the purpose of creating this e-commerce project.  In reality, a true e-commerce store would most likely have original photos which aligned better in terms of content and size.

## Faceted Filtering
The developer attempted to mimic a common feature in e-commerce websites, which is to provide users faceted filtering of products, in order to narrow down their view of products. With each filter that is applied, the list of products becomes more relevant to the user. 

This was achieved by maintaining the previous filter criteria when applying another.  When products are narrowed down by plant category - for example, floor plants - this criteria is maintained when filtering again by, for example, price.  

With this method, the search criteria in the webpage url maintains the previous criteria, but is overridden with the new criteria as the querydict recognises the last value.  The example below shows the list of products filtered by 'Floor' plants, then the search criteria is changed to 'Hanging' plants, but the url still shows the previous filter.  Since 'Hanging' plants is the last value of the plant category filters, 'Floor' is ignored and only 'Hanging' plants are listed.

This method in general provides a good solution to faceted filtering, although may be somewhat verbose. See [testing](TESTING.md#2.3) for this user feature. 

![Faceted searching](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652450462/LovePlants/Products/faceted_kdwlyo.jpg)

## Like Product
In order to allow users to 'like' products, a heart icon is rendered on the product card in the products page - solid white if not liked, solid black if liked.  Inconsistency in product image backgrounds result in a poor contrast of this heart on some product cards.  

Good contrast:
![Good contrast](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652345634/LovePlants/goodcontrast_mrjohi.jpg)
![Good contrast](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652345707/LovePlants/goodcontrast2_lvoppz.jpg)

Poor contrast:
![Poor contrast](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652345633/LovePlants/poorcontrast_n7lpt1.jpg)
![Poor contrast](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1652345706/LovePlants/poorcontrast2_ybstdh.jpg)

Possible solutions to this are:
- better consistency with image backgrounds, in a true e-commerce site the images should be far more consistent
- place the heart icon somewhere in the product card text, as opposed to within the image
- use a different icon, a black outline heart icon with a white background (not free on Font Awesome), as opposed to a solid icon in white or black

[Back to top](#love-plants)

# Media

## Images
Images used on the site were sourced from the following sources.  Images which are free to use publicy were desirable, however when this was not possible the images are credited.

Product images are credited appropriately in the product model (image1_source_url etc).

Pexels was a fantastic resource for sourcing high quality banner images.  The content came from the below creators:
- cottonbro
- karolina-grabowska
- khanh-nguyen
- huy-phan
- staphanie-ho
- mentatdgt
- daria-shevtsova
- designecologist
- element-digital
- sohail-nachiti

The Spruce gardening website was used extensively to source project images and descriptions.

[Back to top](#love-plants)

# Credits

## Technologies
- [Github](https://github.com/)
- [Gitpod](https://gitpod.io/)
- [Postgres](https://www.postgresql.org/)
- [Bootstrap 5.0](https://getbootstrap.com/docs/5.0)
- [Django](https://www.djangoproject.com/)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [Python 3.8](https://www.python.org/)
- [Javascript](https://www.javascript.com/)
- [HTML](https://en.wikipedia.org/wiki/HTML)

## Media
- [Cloudinary](https://cloudinary.com/console/)
- [Pexels](https://www.pexels.com/)
- [The Spruce](https://www.thespruce.com/)

## Design
- [Balsamiq](https://balsamiq.com/)
- [QuickDBD](https://www.quickdatabasediagrams.com/)

## Editors
- [Python Online Editor](https://www.online-python.com/)
- [JS Beautifier](https://jsonformatter.org/jsbeautifier)

## Content
- [Harper Collins](https://harpercollins.co.uk/pages/ecommerce-faqs)
- [Google Fonts](https://fonts.google.com/)
- [Flaticon Plant Images](https://www.flaticon.com/packs/indoor-plants-1)
- [Font Awesome](https://fontawesome.com/)

## Generators
- [Terms and Conditions generator](https://www.termsandconditionsgenerator.com/) \
- [Privacy Policy generator](https://www.privacypolicygenerator.info/)
- [Markdown ToC Generator](https://luciopaiva.com/markdown-toc/)
- [Responsive Design](http://ami.responsivedesign.is/)

## SEO
- [Word Tracker](https://www.wordtracker.com/)
- [XML Sitemaps](https://www.xml-sitemaps.com/)
- [Google Mobile-Friendly Test](https://search.google.com/test/mobile-friendly)
- [Mind Map Creator](https://www.canva.com/graphs/mind-maps/)

## Validators
- [W3 Spellchecker](https://www.w3.org/2002/01/spellchecker)
- [Chrome dev tools](https://developers.google.com/web/tools/chrome-devtools)
- [PEP8](http://pep8online.com/)
- [JSHINT](https://jshint.com/)
- [W3C](https://validator.w3.org/)
- [W3 Jigsaw](https://jigsaw.w3.org/css-validator/)

## Marketing
- [Mailchimp](https://us18.admin.mailchimp.com/)
- [Facebook](https://www.facebook.com/)
- [Temp Mail](https://tempmail.net/)

# Acknowledgements

- I'd like to thank my mentor, Mo Shami, for providing me support throughout the development of this project.
- I'd like to thank tutor support at Code Institute for many hours of technical help.
- I'd like to thank my family for taking time to use my project website and providing me helpful feedback. 

# Disclaimers

- This project was created for educational purposes only for the Code Institute Full Stack Development course.
- This project includes text content and images sourced from other websites, all of which are credited appropriately. The developer does not own any of the images. 
- There may be some minor styling differences between images in this ReadMe file and the final deployed website.

[Back to top](#love-plants)