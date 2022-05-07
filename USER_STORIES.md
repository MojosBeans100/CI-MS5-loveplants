
# User Stories
This document lists all user stories for the project.  
Testing of these user stories can be found [here](TESTING.md).
These user stories and associated milestones, sprints and project boards can be found [here](https://github.com/MojosBeans100/CI-MS5-loveplants).

## Table of Contents
- [User Stories](#user-stories)
  - [Table of Contents](#table-of-contents)
  - [User Story 1](#user-story-1)
    - [1.1](#11)
    - [1.2](#12)
    - [1.3](#13)
    - [1.4](#14)
    - [1.5](#15)
    - [1.6](#16)
  - [User Story 2](#user-story-2)
    - [2.1](#21)
    - [2.2](#22)
    - [2.3](#23)
    - [2.4](#24)
    - [2.5](#25)
    - [2.6](#26)
  - [User Story 3](#user-story-3)
    - [3.1](#31)
    - [3.2](#32)
    - [3.3](#33)
    - [3.4](#34)
    - [3.5](#35)
    - [3.6](#36)
  - [User Story 4](#user-story-4)
    - [4.1](#41)
    - [4.2](#42)
    - [4.3](#43)
    - [4.4](#44)
    - [4.5](#45)
  - [User Story 5](#user-story-5)
    - [5.1](#51)
    - [5.2](#52)
    - [5.3](#53)
  - [User Story 6](#user-story-6)
    - [6.1](#61)
    - [6.2](#62)
    - [6.3](#63)
    - [6.4](#64)
    - [6.5](#65)

## User Story Strategy

### EPICS > User Stories > Tasks
User stories were derived from the determined EPICS for an e-commerce store, which were:

 - Account authentication, to allow users to create an account
 - List/view products, to display all products availabe for sale
 - Add products to shopping bag, to allow users to create a record of items they wish to purchase
 - Checkout bag, to allow users to buy products
 - Ratings and reviews, to allow users to have their opinion about products
 - Admin accessibility, to allow admin users to modify the database of products

These EPICS were refined into shorter User Stories, which could be broken down into tasks for the developer to complete within the defined sprint or milestone.  

### User Story Priority Labels
User Stories were assigned labels, based on the anticipated priority of completion.  

- User Stories deemed crucial to meet the requirements of the sprint were labelled 'Must Have'.
- User Stories deemed important but not necessary were labelled 'Should Have'.
- User Stories deemed worthwhile but could be completed at a later date were labelled 'Could Have'.
- User Stories which were determined could not be completed in the sprint were labelled 'Won't Have'.
- User Stories which could only be partially completed (for example, they required other aspects of the site to be up and running in order to complete), generally had a 'Should Have' or 'Could Have' label, with a secondary 'Won't Have' label added later.  These User Stories were then featured on a later sprint in order to complete. 

Any User Stories which did not feature in the final deployed project were always either 'Should Have' or more likely 'Could Have', thus did not affect the integrity of the website by being omitted. 

### Acceptance Criteria
Clear acceptance criteria for all User Stories were defined, and were not marked as complete until all criteria were met.  The acceptance criteria also determined the strategy for testing.

## User Story 1
User Story 1 is based on allow users account authentication on the website. 

### 1.1 
As a **site user** I can **create an account to LovePlants with a username, email address and password** so that **I can access personal information and historic orders**

Acceptance Criteria:
- New users can create a new account to LovePlants
- Returning users can return to their account to LovePlants
- Users can log out of their account

### 1.2
As a **site user** I can **see my current login status on all pages** so that **I am aware if my account is active or if I need to log in**

Acceptance Criteria:
- Users can clearly see how to sign up
- Users can see their log in status in the navigation bar on all pages

### 1.3
As a **site user** I can **navigate to a page which details my personal information** so that **I can see my details pertaining to my personal account on LovePlants**

Acceptance Criteria:
- Users are aware how to reach the page for their personal account
- Users can see relevant information about their account on their account page
- Only the active user can access their account page

### 1.4
As a **site user** I can **access information of my previous orders** so that **I can see when I last ordered, how many orders I have, see the details of previous orders**

Acceptance Criteria:
- Users can see a list of their previous orders in their account page
- Users are aware of the relevant details of previous orders (total, quantity items, date ordered)
- Users can click on each order to view the details of the order

### 1.5
As a **site user** I can **update my personal information such as delivery information** so that **I can change details as needed, and save default information**

Acceptance Criteria:
- Users can access details about their account to be updated, and adjust as needed
- Users cannot access details which cannot be changed
- Users are immediately aware when their details have been changed

### 1.6
As a **site user** I can **I can delete my account when I no longer need it** so that **I am removed from the LovePlants website**

Acceptance Criteria:
- Users can delete their account from LovePlants
- Users are aware when their account has been deleted
- Users are given a chance to change their mind before deleting their account
- Users are aware of the consequences of deleting their account


## User Story 2
User Story 2 involves allowing users to view, filter and search for products.

### 2.1
As a **site user** I can **I can view a list of all available products to buy** so that **I can see the selection of products on the website**

Acceptance Criteria:
- Users can view products available to buy
- Users can see a picture, product name, price for the product
- Users can see how many products they are viewing

### 2.2
As a **site user** I can ** I can use a search bar to input product details** so that **I can search for a specific product**

Acceptance Criteria:
- Users can see a search bar at the top of the product list page
- Users can input text into the search bar and press the 'search' button
- Products are filtered by the search text criteria, all other products are not displayed
- Users can see how many products are left in the list after searching
- Users can remove the search functionality to return to all products

### 2.3
As a **site user** I can **I can filter the available products by category etc** so that **the product list contains only products I am interested in**

Acceptance Criteria:
- Users can see categories on buttons on product list page
- When buttons are clicked, only products in that category are displayed
- Users can remove this filter to revert to viewing all products
- Users can see how many products are left in the list after filtering

### 2.4
As a **site user** I can **sort the available products by price and other features** so that **the product list is a more accessible and relevant order to view**

Acceptance Criteria:
- Users can access 'sort by' buttons in the product list page
- Users can change the order of the product list by sorting
- Users can sort by price, name A-Z, rating, popularity
- Users can remove the sorting criteria

### 2.5
As a **site user** I can **view the specific details of a product** so that **I can learn more about products I may wish to purchase**

Acceptance Criteria:
- User can click on product cards in products view to see detail about the product
- User is clearly aware which product they are looking at
- User can see price of product
- User can see how to add this product to their shopping bag

### 2.6
As a **site user** I can **see products which are out of stock** so that **I can see which products may be available in the future**

Acceptance Criteria:
- Users can see which products are out of stock/back soon
- (optional) Users can save these products for later

## User Story 3
User Story 3 captures the requirements for users to add products to their shopping bag and checkout. 

### 3.1
As a **site user** I can **add a product to my shopping bag** so that **I can purchase the item**

Acceptance Criteria:
- User can click on 'Add to Bag' to add the product
- User can determine the quantity of this product they want to add to their bag

### 3.2
As a **site user** I can **I can see a visual pop-up when a product has been added to my shopping bag** so that **I have confirmation that the product has been added**

Acceptance Criteria:
- User received a notification that an item was added to their bag
- User can see the contents of their bag
- User can dismiss the notification
- User can see their shopping bag contents change in the nav bar 

### 3.3
As a **site user** I can **see the total cost of my shopping bag change when I have added a product** so that **I'm aware of the running cost as I add products**

Acceptance Criteria:
- User can see the total of their shopping bag in the nav bar
- User can see the total including delivery in the bag view
- User can see subtotals for individual items in their bag
- User can see notification messages each time the bag total changes

### 3.4
As a **site user** I can **click on my shopping bag** so that **I can view a list of the products I have added**

Acceptance Criteria:
- Users can see all items in their shopping bag
- Users can see information associated with the product ie price, quantity
- Users can see the subtotal of items if there is more than 1
- Users can see a total price of their bag
- Users can see the delivery cost, and how much more is needed to spend in order to qualify for free delivery
- Users are suggested products they could add to the bag which would quality them for free delivery

### 3.5
As a **site user** I can **edit the items in my shopping bag** so that **I can adjust the contents of my bag as needed**

Acceptance Criteria:
- Users can see how to update items in their bag
- [x] Users can see the bag total change when items are updated
- User can see a confirmation message that they edited their item

### 3.6
As a **site user** I can **delete items from my shopping bag** so that **I can remove items I no longer want**

Acceptance Criteria:
- User can see how to delete an item in their bag
- User can no longer see the item in their bag once removed
- User can see a confirmation message that item has been deleted
- User can see updated totals of their bag
- User can see how to re-add the item if deleting was an accident

## User Story 4
User Story 4 captures the full checkout process.

### 4.1
As a **site user** I can **select checkout from my shopping bag** so that **I can buy the products in my bag**

Acceptance Criteria:
- User can proceed to checkout from bag page and notification bar
- User can enter their delivery/billing information and card details
- User is aware when their billing/card details are not valid
- User is directed to a confirmation page upon successful checkout, rendering relevant details
- User is aware if and why their checkout was not successful

### 4.2
As a **site user** I can **verify the order information before I commit to buy** so that **I can check the contents of my bag**

Acceptance Criteria:
- Users can see all products in their bag when on the checkout page
- Users can delete items from their bag on the checkout page

### 4.3
As a **site user** I can **see the total amount my card will be billed** so that **I know how much I am spending from my account**

Acceptance Criteria:
- User knows that pressing Secure Checkout/Submit will charge their card details
- Users knows how much money will be taken from their card
- User can see the charge updating as they edit their bag

### 4.4
As a **site user** I can **select whether to save the billing/delivery information for next time** so that **I do not have to repeat this step each time**

Acceptance Criteria:
- g
- g
- g

### 4.5
As a **site user** I can **see confirmation that the order has been successful** so that **I am aware the order went through the system**

Acceptance Criteria:
- g
- g
- g

## User Story 5
User Story 5 refers to features which allow users to leave a review and rating for products.

### 5.1
As a **site user** I can **I can rate products I have purchased** so that **other users can see customer feedback on the product**

Acceptance Criteria:
- User can rate products they have purchased
- Users cannot rate products they have not purchased
- Users cannot rate products more than once

### 5.2
As a **site user** I can **add a comment review to products I have purchased** so that **other users can see a comment from a previous buyer of the product**

Acceptance Criteria:
- Users can comment on products they have purchased
- Users can review comments from other buys

### 5.3
As a **site user** I can **review ratings for products** so that **I can see previous customer's experience with this product**

Acceptance Criteria:
- Users can see a review/rating section on each product detail
- Users can scroll through reviews for a product
- Users can see when the reviews were left

## User Story 6
User Story 6 captures the admin requirements for using the website, to add, edit, delete products.

### 6.1
As a **site admin** I can **edit information about products, such as price, quantity remaining, picture** so that **product details can be adjusted as required**

Acceptance Criteria:
- Admin users can see an 'Edit product' button at the top of the product detail page
- Admin users can adjust details as needed on the edit form
- Admin users can see the changes they made reflected in the product detail page
- Admin users are aware if there is an issue with the changes they made

### 6.2
As a **site admin** I can **add products to the LovePlants store** so that **site users can view and buy new products**

Acceptance Criteria:
- Admin users can click 'Add Product' on the products page
- Admin users can see previously created products which are not live on the website
- Admin users can see placeholders or descriptions so they are aware what the form field represents
- Admin users can fill in Add Product form
- Admin users can submit the form
- Admin users are aware if there is an issue with the from they submitted

### 6.3
As a **site admin** I can **apply a discount to any/all products** so that **LovePlants can sell off old stock, or promote product for special calendar days**

Acceptance Criteria:
- A
- A
- a

### 6.4
As a **site admin** I can **delete products from the LovePlants store** so that **discontinued stock can be removed from the product list**

Acceptance Criteria:
- A
- A
- a

### 6.5
As a **site admin** I can **review, edit and delete customer orders** so that **orders can be adjusted accordingly**

Acceptance Criteria:
- A
- A
- a