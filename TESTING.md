
## Table of contents

- [User Story 1 Testing](#user-story-1-testing)
  - [1.1](#11)
  - [1.2](#12)
  - [1.3](#13)
  - [1.4](#14)
  - [1.5](#15)
  - [1.6](#16)
- [User Story 2 Testing](#user-story-2-testing)
  - [2.1](#21)
  - [2.2](#22)
  - [2.3](#23)
  - [2.4](#24)
  - [2.5](#25)
  - [2.6](#26)
- [User Story 3 Testing](#user-story-3-testing)
  - [3.1](#31)
  - [3.2](#32)
  - [3.3](#33)
  - [3.4](#34)
  - [3.5](#35)
  - [3.6](#36)
- [Validation](#validation)
  - [CSS](#css)
  - [HTML](#html)
  - [Javascript](#javascript)

# Manual Testing

## Overview of manual testing
Comprehensive manual testing was undertaken for this website, to ensure functionality was as expected from the user's point of view.  This testing encompasses the Javascript functions in the front-end of the website, to ensure functions are working as expected and outputting the correct HTML content to the user, as well as the back-end Python code in the Django views and the resulting Postgres database. 

Each user story is tested for large, medium and small screen sizes to ensure the website was responsive for all screen sizes. Acceptance criteria is defined for each user story and the test is considered 'passed' if the acceptance criteria has been met. 

|Screen|Width|Rendered on|
|------|----|---------|
|Desktop (large monitor)|1800px|Chrome Devtools|
|Tablets (iPad Air)|1180px|Chrome Devtools|
|Mobile (iPhone SE)|375px|Chrome Devtools|

Note: since performing manual testing, some minor adjustments may have been made to improve small styling details, which would result in slight differences between images on the deployed site and images of the site contained in this document.  It was ensured any changes did not affect the outcome of the testing.

## User Story 1 Testing
User Story 1 is based on allow users account authentication on the website. 

### 1.1 
As a **site user** I can **create an account to LovePlants with a username, email address and password** so that **I can access personal information and historic orders**

Testing Structure

|User action|Desktop|Tablet|Mobile|Status|
|-----------|-------|------|------|------|
||||||

Acceptance Criteria:
- New users can create a new account to LovePlants
- Returning users can return to their account to LovePlants
- Users can log out of their account
- Users must confirm their email address to access their new account

### 1.2
As a **site user** I can **see my current login status on all pages** so that **I am aware if my account is active or if I need to log in**

|Criteria|Desktop|Tablet|Mobile|Status|
|-----------|-------|------|------|------|
|on any given page, users can see the checkmark next to the profile icon in the navbar|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651237432/LovePlants/Testing/US1/desktop1_ufsqle.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651237432/LovePlants/Testing/US1/tablet1_ksnrzk.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651237432/LovePlants/Testing/US1/mobile1_veelj5.jpg)|Pass|
|upon hover of the profile icon in the navbar, the logged in user's username is displayed|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651237432/LovePlants/Testing/US1/desktop2_qmjfls.png)|N/A|N/A|Pass|
|if the user is not logged in, upon hover of profile icon users are instructed to log in|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651237643/LovePlants/Testing/US1/desktop3_mu4nh9.png)|N/A|N/A|Pass|
|if the user is not logged in, upon clicking the profile icon users are directed to the log in page|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651237680/LovePlants/Testing/US1/desktop4_m1qkur.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651237883/LovePlants/Testing/US1/tablet4_zfk6tq.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651237883/LovePlants/Testing/US1/mobile4_kjtera.jpg)|Pass|

Acceptance Criteria:
- [x] Users can clearly see how to log in
- [x] Users can see their log in status in the navigation bar on all pages

### 1.3
As a **site user** I can **navigate to a page which details my personal information** so that **I can see my details pertaining to my personal account on LovePlants**

|Criteria|Desktop|Tablet|Mobile|Status|
|-----------|-------|------|------|------|
|upon navigating to the users profile, their identifying and account info is displayed|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651240664/LovePlants/Testing/US1/desktop1_cymipd.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651240664/LovePlants/Testing/US1/tablet1_dxupzx.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651240664/LovePlants/Testing/US1/mobile1_ebhzgp.jpg)|Pass|
|non authenticated users are redirected to the home page when attempted to navigated to the profile page via the URL|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651244363/LovePlants/Testing/US1/US%201.3/desktopurl_q32r22.jpg)|N/A|N/A|Pass|

Acceptance Criteria:
- [x] Users are aware how to reach the page for their personal account
- [x] Users can see relevant information about their account on their account page
- [x] Only the active user can access their account page

### 1.4
As a **site user** I can **access information of my previous orders** so that **I can see when I last ordered, how many orders I have, see the details of previous orders**

|Criteria|Desktop|Tablet|Mobile|Status|
|-----------|-------|------|------|------|
|users can see how many orders they have submitted|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651241306/LovePlants/Testing/US1/US%201.4/desktop1_zkhjdl.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651241308/LovePlants/Testing/US1/US%201.4/tablet1_dwweew.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651241307/LovePlants/Testing/US1/US%201.4/mobile1_et6ucy.jpg)|Pass|
|users can see a dropdown with the order reference, date and total price|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651241307/LovePlants/Testing/US1/US%201.4/desktop2_gwuc7p.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651241307/LovePlants/Testing/US1/US%201.4/tablet2_c9l59t.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651241307/LovePlants/Testing/US1/US%201.4/mobile2_bbauh9.jpg)|Pass|
|users can click on the drop down to see further info about the order|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651241307/LovePlants/Testing/US1/US%201.4/desktop3_q8omqq.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651241307/LovePlants/Testing/US1/US%201.4/tablet3_v0dxve.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651241307/LovePlants/Testing/US1/US%201.4/mobile31_yplusf.jpg)<br/>[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651241307/LovePlants/Testing/US1/US%201.4/mobile32_xl8xcd.jpg)|Pass|

Acceptance Criteria:
- [x] Users can see a list of their previous orders in their account page
- [x] Users are aware of the relevant details of previous orders (total, quantity items, date ordered)
- [x] Users can click on each order to view the details of the order

### 1.5
As a **site user** I can **update my personal information such as delivery information** so that **I can change details as needed, and save default information**

|Criteria|Desktop|Tablet|Mobile|Status|
|-----------|-------|------|------|------|
|users can fill in, or edit their default delivery information|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651241953/LovePlants/Testing/US1/1.5/desktop1_oqbyam.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651241953/LovePlants/Testing/US1/1.5/tablet1_ijrfl9.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651241953/LovePlants/Testing/US1/1.5/mobile1_pap57s.jpg)|Pass|
|placeholders are provided in place of field input labels|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651241954/LovePlants/Testing/US1/1.5/desktop12_xoqzcs.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651241953/LovePlants/Testing/US1/1.5/tablet12_mqnxkj.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651241953/LovePlants/Testing/US1/1.5/mobile12_gwwqre.jpg)|Pass|
|users can click Update Details, and see their updated information|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651243748/LovePlants/Testing/US1/1.5/desktop3_p1hqmj.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651243748/LovePlants/Testing/US1/1.5/tablet3_jwywjl.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651243748/LovePlants/Testing/US1/1.5/mobile3_cya3r9.jpg)|Pass|
|users are provided a notification to confirm success of updating their info|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651243748/LovePlants/Testing/US1/1.5/desktop4_kkk4wo.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651243748/LovePlants/Testing/US1/1.5/talet4_i7aeuk.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651243748/LovePlants/Testing/US1/1.5/mobile4_bf8mlf.jpg)|Pass|

Acceptance Criteria:
- [x] Users can access details about their account to be updated, and adjust as needed
- [x] Users cannot access details which cannot be changed
- [x] Users are immediately aware when their details have been changed

### 1.6
As a **site user** I can **I can delete my account when I no longer need it** so that **I am removed from the LovePlants website**

Acceptance Criteria:
- Users can delete their account from LovePlants
- Users are aware when their account has been deleted
- Users are given a chance to change their mind before deleting their account
- Users are aware of the consequences of deleting their account

## User Story 2 Testing
User Story 2 involves allowing users to view, filter and search for products.

### 2.1
As a **site user** I can **I can view a list of all available products to buy** so that **I can see the selection of products on the website**

|Criteria|Desktop|Tablet|Mobile|Status|
|-----------|-------|------|------|------|
|when user navigates to the products page, a list of projects are displayed|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651393182/LovePlants/Testing/US%202/2.1/desktop1_znk5tv.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651393176/LovePlants/Testing/US%202/2.1/tablet1_dqemdj.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651393176/LovePlants/Testing/US%202/2.1/mobile1_ild73b.jpg)|Pass|
|a Bootstrap card is used to identify the product with identifying information|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651393176/LovePlants/Testing/US%202/2.1/desktop2_frirqa.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651393176/LovePlants/Testing/US%202/2.1/tablet2_kf4di0.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651393176/LovePlants/Testing/US%202/2.1/mobile2_ii5ogv.jpg)|Pass|

Acceptance Criteria:
- [x] Users can view products available to buy
- [x] Users can see a picture, product name, price for the product
- [x] Users can see how many products they are viewing

### 2.2
As a **site user** I can **use a search bar to input product details** so that **I can search for a specific product**

|Criteria|Desktop|Tablet|Mobile|Status|
|-----------|-------|------|------|------|
|the search bar is displayed above the products|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651402726/LovePlants/Testing/US%202/2.2/desktop1_ingfer.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651402726/LovePlants/Testing/US%202/2.2/tablet1_stcqri.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651402725/LovePlants/Testing/US%202/2.2/mobile1_exu3m3.jpg)|Pass|
|users can input a search term and press the magnifying glass button|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651402810/LovePlants/Testing/US%202/2.2/desktop3_l9qb7y.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651402810/LovePlants/Testing/US%202/2.2/tablet3_jdrqjk.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651402810/LovePlants/Testing/US%202/2.2/mobile3_tan3ue.jpg)|Pass|
|the product list will narrow down products to only those that contain the search term, which is displayed above the list of products|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651402725/LovePlants/Testing/US%202/2.2/desktop2_sqlno9.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651402726/LovePlants/Testing/US%202/2.2/tablet2_jz5yqq.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651402725/LovePlants/Testing/US%202/2.2/mobile2_lt2rtl.jpg)|Pass|
|upon clicking 'clear all filters' the page is displayed with all products|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651402726/LovePlants/Testing/US%202/2.2/desktop1_ingfer.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651402726/LovePlants/Testing/US%202/2.2/tablet1_stcqri.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651402725/LovePlants/Testing/US%202/2.2/mobile1_exu3m3.jpg)|Pass|

Acceptance Criteria:
- [x] Users can see a search bar at the top of the product list page
- [x] Users can input text into the search bar and press the 'search' button
- [x] Products are filtered by the search text criteria, all other products are not displayed
- [x] Users can see how many products are left in the list after searching
- [x] Users can remove the search functionality to return to all products

### 2.3
As a **site user** I can **I can filter the available products by category etc** so that **the product list contains only products I am interested in**

|Criteria|Desktop|Tablet|Mobile|Status|
|-----------|-------|------|------|------|
|users can click on any of the plant icons to filter by plant type|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651405964/LovePlants/Testing/US%202/2.3/desktop1_atoojj.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651405964/LovePlants/Testing/US%202/2.3/tablet1_qngtma.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651405964/LovePlants/Testing/US%202/2.3/mobile1_covii9.jpg)|Pass|
|once filtered by plant type, the list narrows down to include only products of that plant type|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651406084/LovePlants/Testing/US%202/2.3/desktop2_fchhqk.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651405964/LovePlants/Testing/US%202/2.3/tablet2_lyxnd2.jpg) [Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651405964/LovePlants/Testing/US%202/2.3/tablet2_lyxnd2.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651405964/LovePlants/Testing/US%202/2.3/mobile2_zivpet.jpg) [Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651405964/LovePlants/Testing/US%202/2.3/mobile3_tyc1kj.jpg)|Pass|
|users can further narrow the list by filtering by other criteria, such as price|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651406430/LovePlants/Testing/US%202/2.3/desktop3_de8i8z.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651406430/LovePlants/Testing/US%202/2.3/tablet3_faqngx.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651406430/LovePlants/Testing/US%202/2.3/mobile4_htvyej.jpg) []Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651406430/LovePlants/Testing/US%202/2.3/mobile5_i5l5k3.jpg)|Pass|


Acceptance Criteria:
- [x] Users can see categories on buttons on product list page
- [x] When buttons are clicked, only products in that category are displayed
- [x] Users can remove this filter to revert to viewing all products
- [x] Users can see how many products are left in the list after filtering

### 2.4
As a **site user** I can **sort the available products by price and other features** so that **the product list is a more accessible and relevant order to view**

|Criteria|Desktop|Tablet|Mobile|Status|
|-----------|-------|------|------|------|
|users can click on the drop down to sort by criteria|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651407179/LovePlants/Testing/US%202/2.4/desktop1_z95qcr.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651407179/LovePlants/Testing/US%202/2.4/tablet1_bwrv0x.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651407179/LovePlants/Testing/US%202/2.4/mobile1_ba5ced.jpg)|Pass|
|when sorting criteria is chosen, the products rearrange to adhere to that criteria|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651407179/LovePlants/Testing/US%202/2.4/desktop3_vd636u.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651407179/LovePlants/Testing/US%202/2.4/tablet2_bgyoyp.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651407179/LovePlants/Testing/US%202/2.4/mobile2_jvez0y.jpg)|Pass|
|clicking 'Clear all' removes the sorting criteria|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651407297/LovePlants/Testing/US%202/2.4/desktop2_k2szzq.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651407297/LovePlants/Testing/US%202/2.4/tablet3_dqtbpu.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651407297/LovePlants/Testing/US%202/2.4/mobile3_wfjjd6.jpg)|Pass|

Acceptance Criteria:
- [x] Users can access 'sort by' buttons in the product list page
- [x] Users can change the order of the product list by sorting
- [x] Users can sort by price, name A-Z, rating, popularity
- [x] Users can remove the sorting criteria

### 2.5
As a **site user** I can **view the specific details of a product** so that **I can learn more about products I may wish to purchase**

|Criteria|Desktop|Tablet|Mobile|Status|
|-----------|-------|------|------|------|
|users can click on any product which will direct them to the detail page.  Upon hover, a second image is displayed|||||
|upon navigating to the product detail, the user can see the name, category, price and images of the product|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651410246/LovePlants/Testing/US%202/2.5/desktop1_zln4j8.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651410246/LovePlants/Testing/US%202/2.5/tablet1_sl43ri.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651410245/LovePlants/Testing/US%202/2.5/mobile1_ujfz0e.jpg) [Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651410246/LovePlants/Testing/US%202/2.5/mobile2_wfb6kn.jpg)|Pass|
|images can be clicked to reveal a larger size|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651412029/LovePlants/Testing/US%202/2.5/desktop3_wjwtf0.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651412029/LovePlants/Testing/US%202/2.5/tablet3_osoh7r.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651412029/LovePlants/Testing/US%202/2.5/mobile4_cw8jls.jpg)|Pass|
|the care instructions are provided|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651410246/LovePlants/Testing/US%202/2.5/desktop2_aqt5rf.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651410246/LovePlants/Testing/US%202/2.5/tablet1_sl43ri.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651410246/LovePlants/Testing/US%202/2.5/mobile3_o1ozn7.jpg)|Pass|

Acceptance Criteria:
- [x] User can click on product cards in products view to see detail about the product
- [x] User is clearly aware which product they are looking at
- [x] User can see price of product, care details, reviews
- [x] User can see how to add this product to their shopping bag

### 2.6
As a **site user** I can **see products which are out of stock** so that **I can see which products may be available in the future**

Acceptance Criteria:
- Users can see which products are out of stock/back soon
- (optional) Users can save these products for later

## User Story 3 Testing
User Story 3 captures the requirements for users to add products to their shopping bag and checkout. 

### 3.1
As a **site user** I can **add a product to my shopping bag** so that **I can purchase the item**

|Criteria|Desktop|Tablet|Mobile|Status|
|-----------|-------|------|------|------|
|users can see an 'Add to bag' button on the product page|[Desktop]()|[Tablet]()|[Mobile]()|Pass|
|users can change the quantity of the product to add|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651414942/LovePlants/Testing/US%203/3.1/desktop2_yicahh.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651414942/LovePlants/Testing/US%203/3.1/tablet2_jzipkm.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651414942/LovePlants/Testing/US%203/3.1/mobile2_eyoqtb.jpg)|Pass|
|users can see a notification that the product was added to their bag|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651414942/LovePlants/Testing/US%203/3.1/desktop1_xtuvsa.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651414942/LovePlants/Testing/US%203/3.1/tablet1_tmoe9i.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651414942/LovePlants/Testing/US%203/3.1/mobile1_w3mh7l.jpg)|Pass|
|in the bag itself, users can click 'Quick Add' to add further items to their bag|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651414942/LovePlants/Testing/US%203/3.1/desktop3_otomoj.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651414943/LovePlants/Testing/US%203/3.1/tablet3_m8h2tk.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651414942/LovePlants/Testing/US%203/3.1/mobile3_rcv0aj.jpg)|Pass|

Acceptance Criteria:
- User can click on 'Add to Bag' to add the product
- User can determine the quantity of this product they want to add to their bag

### 3.2
As a **site user** I can **I can see a visual pop-up when a product has been added to my shopping bag** so that **I have confirmation that the product has been added**

|Criteria|Desktop|Tablet|Mobile|Status|
|-----------|-------|------|------|------|
|users receive a notification|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651479335/LovePlants/Testing/US%203/3.2%20/desktop12_p1wqyw.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651479334/LovePlants/Testing/US%203/3.2%20/tablet12_a83l3r.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651479334/LovePlants/Testing/US%203/3.2%20/mobile12_wyq7f2.jpg)|Pass|
|users see the contents of their shopping bag|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651479335/LovePlants/Testing/US%203/3.2%20/desktop12_p1wqyw.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651479334/LovePlants/Testing/US%203/3.2%20/tablet12_a83l3r.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651479334/LovePlants/Testing/US%203/3.2%20/mobile12_wyq7f2.jpg)|Pass|
|users can click the 'X' to dimiss the notification and continue shopping|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651479335/LovePlants/Testing/US%203/3.2%20/desktop3_hsjnnd.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651479334/LovePlants/Testing/US%203/3.2%20/tablet3_ouccyf.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651479334/LovePlants/Testing/US%203/3.2%20/mobile3_yfaq5d.jpg)|Pass|
|users see the number of items in their bag change|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651479334/LovePlants/Testing/US%203/3.2%20/desktop4_fhemvp.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651479334/LovePlants/Testing/US%203/3.2%20/tablet4_qpmxyn.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651479334/LovePlants/Testing/US%203/3.2%20/mobile3_yfaq5d.jpg)|Pass|

Acceptance Criteria:
- [x] User received a notification that an item was added to their bag
- [x] User can see the contents of their bag
- [x] User can dismiss the notification
- [x] User can see their shopping bag contents change in the nav bar 

### 3.3
As a **site user** I can **see the total cost of my shopping bag change when I have added a product** so that **I'm aware of the running cost as I add products**

|Criteria|Desktop|Tablet|Mobile|Status|
|-----------|-------|------|------|------|
|the navbar displays the number of items in the user's bag|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651482531/LovePlants/Testing/US%203/3.3/dekstop1_hljbch.jpg) [Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651482531/LovePlants/Testing/US%203/3.3/desktop12_qnh2wt.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651482708/LovePlants/Testing/US%203/3.3/tablet1_i1jsvd.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651482708/LovePlants/Testing/US%203/3.3/mobile123_vt208m.jpg)|Pass|
|the bag total is itemised|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651482531/LovePlants/Testing/US%203/3.3/desktop2_ko7zbs.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651482708/LovePlants/Testing/US%203/3.3/tablet2_urkfuf.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651482708/LovePlants/Testing/US%203/3.3/mobile123_vt208m.jpg)|Pass|
|subtotals are displayed for each product|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651482531/LovePlants/Testing/US%203/3.3/desktop3_wnqnxc.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651482708/LovePlants/Testing/US%203/3.3/tablet2_urkfuf.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651482708/LovePlants/Testing/US%203/3.3/mobile123_vt208m.jpg)|Pass|
|notifications provide updated bag total|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651482531/LovePlants/Testing/US%203/3.3/desktop4_ka3kec.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651482708/LovePlants/Testing/US%203/3.3/tablet4_na3pkf.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651482708/LovePlants/Testing/US%203/3.3/mobile4_ansrs3.jpg)|Pass|

Acceptance Criteria:
- [x] User can see the total number of products of their shopping bag in the nav bar
- [x] User can see the total including delivery in the bag view
- [x] User can see subtotals for individual items in their bag
- [x] User can see notification messages each time the bag total changes

### 3.4
As a **site user** I can **click on my shopping bag** so that **I can view a list of the products I have added**

|Criteria|Desktop|Tablet|Mobile|Status|
|-----------|-------|------|------|------|
|in the bag page, user can see items, quantities, subtotals|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651485184/LovePlants/Testing/US%203/3.4/desktop12345_o5rtyp.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651485184/LovePlants/Testing/US%203/3.4/tablet_gyotqu.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651485184/LovePlants/Testing/US%203/3.4/mobile1_u5zncg.jpg)|Pass|
|users are suggested products which, by adding, would reduce delivery charge to £0|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651485183/LovePlants/Testing/US%203/3.4/desktop6_qg1c2t.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651485184/LovePlants/Testing/US%203/3.4/tablet2_zdmccf.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651485184/LovePlants/Testing/US%203/3.4/mobile2_gasahr.jpg)|Pass|
|by adding one of these products, delivery is reduced to £0|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651485183/LovePlants/Testing/US%203/3.4/desktop3_u7dilg.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651485184/LovePlants/Testing/US%203/3.4/tablet3_ulvx6x.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651485184/LovePlants/Testing/US%203/3.4/mobile3_shf2ul.jpg)|Pass|

Acceptance Criteria:
- [x] Users can see all items in their shopping bag
- [x] Users can see information associated with the product ie price, quantity
- [x] Users can see the subtotal of items if there is more than 1
- [x] Users can see a total price of their bag
- [x] Users can see the delivery cost, and how much more is needed to spend in order to qualify for free delivery
- [x] Users are suggested products they could add to the bag which would quality them for free delivery

### 3.5
As a **site user** I can **edit the items in my shopping bag** so that **I can adjust the contents of my bag as needed**

|Criteria|Desktop|Tablet|Mobile|Status|
|-----------|-------|------|------|------|
|users can see the current quantity in their bag|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651489084/LovePlants/Testing/US%203/3.5/desktop1_yaotvt.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651489085/LovePlants/Testing/US%203/3.5/tablet1_okslse.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651489084/LovePlants/Testing/US%203/3.5/mobile1_i2ytkh.jpg)|Pass|
|users can input a new quantity|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651489084/LovePlants/Testing/US%203/3.5/desktop2_cuil3t.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651489085/LovePlants/Testing/US%203/3.5/tablet3_bjerdr.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651489084/LovePlants/Testing/US%203/3.5/mobile2_nwkuxi.jpg)|Pass|
|users can see the updated quantity in their bag|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651489084/LovePlants/Testing/US%203/3.5/desktop3_lfmaev.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651489085/LovePlants/Testing/US%203/3.5/tablet3_bjerdr.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651489084/LovePlants/Testing/US%203/3.5/mobile3_k7qr4s.jpg)|Pass|
|a notification is shown that the item has been updated|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651489084/LovePlants/Testing/US%203/3.5/desktop4_vqqmak.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651489085/LovePlants/Testing/US%203/3.5/tablet4_af8q8z.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651489084/LovePlants/Testing/US%203/3.5/mobile4_mtzb4v.jpg)|Pass|

Acceptance Criteria:
- [x] Users can see how to update items in their bag
- [x] Users can see the bag total change when items are updated
- [x] User can see a confirmation message that they edited their item

### 3.6
As a **site user** I can **delete items from my shopping bag** so that **I can remove items I no longer want**

|Criteria|Desktop|Tablet|Mobile|Status|
|-----------|-------|------|------|------|
|users can see a trash can icon in the bag page|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651490418/LovePlants/Testing/US%203/3.6/desktop1_jpo6qr.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651490419/LovePlants/Testing/US%203/3.6/tablet1_vw9s7t.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651490418/LovePlants/Testing/US%203/3.6/mobile1_p6klgt.jpg)|Pass|
|users can see that the item was removed from their bag|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651490418/LovePlants/Testing/US%203/3.6/desktop23_qwab1i.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651490419/LovePlants/Testing/US%203/3.6/tablet234_bscd3c.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651490418/LovePlants/Testing/US%203/3.6/mobile2_fbyzko.jpg)|Pass|
|users can see a notification that the item was removed|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651490418/LovePlants/Testing/US%203/3.6/desktop23_qwab1i.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651490419/LovePlants/Testing/US%203/3.6/tablet234_bscd3c.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651490418/LovePlants/Testing/US%203/3.6/mobile3_uygxxj.jpg)|Pass|
|users can see a trash can icon in the bag notification|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651490418/LovePlants/Testing/US%203/3.6/desktop23_qwab1i.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651490419/LovePlants/Testing/US%203/3.6/tablet234_bscd3c.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651490419/LovePlants/Testing/US%203/3.6/mobile4_yimfeo.jpg)|Pass|
|users can click the trash can in the notification to delete the item|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651490418/LovePlants/Testing/US%203/3.6/desktop5_pkm4ad.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651490419/LovePlants/Testing/US%203/3.6/tablet5_j6mhz7.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651490512/LovePlants/Testing/US%203/3.6/mobile5_ojewze.jpg)|Pass|

Acceptance Criteria:
- [x] User can see how to delete an item in their bag
- [x] User can no longer see the item in their bag once removed
- [x] User can see a confirmation message that item has been deleted
- [x] User can see updated totals of their bag
- [x] User can see how to re-add the item if deleting was an accident

## User Story 4 Testing
User Story 4 captures the full checkout process.

### 4.1
As a **site user** I can **select checkout from my shopping bag** so that **I can buy the products in my bag**

|Criteria|Desktop|Tablet|Mobile|Status|
|-----------|-------|------|------|------|
|users can see the checkout button in the bag page|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651578640/LovePlants/Testing/US%204/4.1/desktop1_rdxedk.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651578640/LovePlants/Testing/US%204/4.1/tablet1_lxhxfv.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651578640/LovePlants/Testing/US%204/4.1/mobile1_mytxul.jpg)|Pass|
|users can see the checkout button in the notification bar|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651578640/LovePlants/Testing/US%204/4.1/desktop2_pusiah.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651578641/LovePlants/Testing/US%204/4.1/tablet2_t0sqx5.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651578640/LovePlants/Testing/US%204/4.1/mobile2_guegr5.jpg)|Pass|
|users can fill in their delivery details|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651578940/LovePlants/Testing/US%204/4.1/desktop3_nsvbxd.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651578939/LovePlants/Testing/US%204/4.1/tablet3_ogiad4.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651578940/LovePlants/Testing/US%204/4.1/mobile3_cdhw1q.jpg)|Pass|
|users can see when a field is invalid, with red text|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651578940/LovePlants/Testing/US%204/4.1/desktop4_tk6p8w.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651578940/LovePlants/Testing/US%204/4.1/tablet4_on2mnh.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651578939/LovePlants/Testing/US%204/4.1/mobile4_krseoj.jpg)|Pass|

Acceptance Criteria:
- [x] User can proceed to checkout from bag page and notification bar
- [x] User can enter their delivery/billing information and card details
- [x] User is aware when their billing/card details are not valid

### 4.2
As a **site user** I can **verify the order information before I commit to buy** so that **I can check the contents of my bag**

|Criteria|Desktop|Tablet|Mobile|Status|
|-----------|-------|------|------|------|
|users can see the contents of their bag in the checkout page|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651589432/LovePlants/Testing/US%204/4.2/desktop1_r6f45g.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651589432/LovePlants/Testing/US%204/4.2/tablet1_k29fmz.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651589431/LovePlants/Testing/US%204/4.2/mobile1_olk4s1.jpg)|Pass|
|users can delete items from this page, remove items from their bag|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651589432/LovePlants/Testing/US%204/4.2/desktop2_ifzr0b.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651589432/LovePlants/Testing/US%204/4.2/tablet2_owk6zi.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651589432/LovePlants/Testing/US%204/4.2/mobile2_xdoy5c.jpg)|Pass|

Acceptance Criteria:
- [x] Users can see all products in their bag when on the checkout page
- [x] Users can delete items from their bag on the checkout page

### 4.3
As a **site user** I can **see the total amount my card will be billed** so that **I know how much I am spending from my account**

|Criteria|Desktop|Tablet|Mobile|Status|
|-----------|-------|------|------|------|
|users can see the grand total of their shopping bag on the checkout page|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651590013/LovePlants/Testing/US%204/4.3/desktop_jnb6w4.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651590013/LovePlants/Testing/US%204/4.3/tablet_ceov09.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651590013/LovePlants/Testing/US%204/4.3/mobile_f0lptu.jpg)|Pass|
|users can see the 'your card will be charged' prompt beneath the 'Secure Checkout' button|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651590013/LovePlants/Testing/US%204/4.3/desktop_jnb6w4.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651590013/LovePlants/Testing/US%204/4.3/tablet_ceov09.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651590013/LovePlants/Testing/US%204/4.3/mobile_f0lptu.jpg)|Pass|
|when the bag contents change, the grand total value changes|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651590180/LovePlants/Testing/US%204/4.3/desktop2_p30zmr.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651590180/LovePlants/Testing/US%204/4.3/tablet2_upmyn0.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651590180/LovePlants/Testing/US%204/4.3/mobile3_xbcrr1.jpg)|Pass|

Acceptance Criteria:
- [x] User knows that pressing Secure Checkout/Submit will charge their card details
- [x] Users knows how much money will be taken from their card
- [x] User can see the charge updating as they edit their bag

### 4.4
As a **site user** I can **select whether to save the billing/delivery information for next time** so that **I do not have to repeat this step each time**

|Criteria|Desktop|Tablet|Mobile|Status|
|-----------|-------|------|------|------|
|users can select 'save information' on the checkout page|[Desktop]()|[Tablet]()|[Mobile]()|Pass|
|the information is saved for next time they checkout|[Desktop]()|[Tablet]()|[Mobile]()|Pass|

Acceptance Criteria:
- 

### 4.5
As a **site user** I can **see confirmation that the order has been successful** so that **I am aware the order went through the system**

|Criteria|Desktop|Tablet|Mobile|Status|
|-----------|-------|------|------|------|
||[Desktop]()|[Tablet]()|[Mobile]()|Pass|
|the user can see their order details on the confirmation page|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651590701/LovePlants/Testing/US%204/4.4/desktop5_p41mil.jpg) [Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651590701/LovePlants/Testing/US%204/4.4/desktop6_bh5qmt.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651590701/LovePlants/Testing/US%204/4.4/tablet5_z3mgay.jpg) [Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651590701/LovePlants/Testing/US%204/4.4/tablet6_rnhjsc.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651590701/LovePlants/Testing/US%204/4.4/mobile5_ao2gj3.jpg) [Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651590816/LovePlants/Testing/US%204/4.4/mobile2_zdi3c0.jpg)|Pass|
||[Desktop]()|[Tablet]()|[Mobile]()|Pass|

Acceptance Criteria:
- User sees a loading screen for confirmation that their order is being processed
- User is directed to a confirmation page upon successful checkout, rendering relevant details
- User is aware if and why their checkout was not successful

## Automated Testing

### Coverage Report
|Module|statements|missing|excluded|coverage|
|------|----------|-------|--------|--------|
bag/__init__.py|	0|	0	0	100%
bag/admin.py|	1|	0	0	100%
bag/apps.py|	4|	0	0	100%
bag/contexts.py|	36|	14	0	61%
bag/migrations/__init__.py|	0|	0	0	100%
bag/models.py|	1|	0	0	100%
bag/test_views.py|	6|	6	0	0%
bag/tests.py|	1|	1	0	0%
bag/urls.py|	3|	0	0	100%
bag/views.py|	56|	49	0	12%
checkout/__init__.py|	1|	0	0	100%
checkout/admin.py|	11|	0	0	100%
checkout/apps.py|	6|	0	0	100%
checkout/forms.py|	16|	9	0	44%
checkout/models.py|	53|	6	0	89%
checkout/signals.py|	9|	1	0	89%
checkout/tests.py|	1|	1	0	0%
checkout/urls.py|	4|	0	0	100%
checkout/views.py|	78|	59	0	24%
checkout/webhook_handler.py|	74|	59	0	20%
checkout/webhooks.py|	28|	19	0	32%
env.py|	7|	0	0	100%
home/__init__.py|	0|	0	0	100%
home/admin.py|	1|	0	0	100%
home/apps.py|	4|	0	0	100%
home/migrations/__init__.py|	0|	0	0	100%
home/models.py|	1|	0	0	100%
home/test_views.py|	6|	6	0	0%
home/tests.py|	1|	1	0	0%
home/urls.py|	3|	0	0	100%
home/views.py|	3|	1	0	67%
loveplants/__init__.py|	0|	0	0	100%
loveplants/asgi.py|	4|	4	0	0%
loveplants/settings.py|	45|	0	0	100%
loveplants/urls.py|	3|	0	0	100%
loveplants/wsgi.py|	4|	4	0	0%
manage.py|	12|	2	0	83%
products/__init__.py|	0|	0	0	100%
products/admin.py|	10|	0	0	100%
products/apps.py|	4|	0	0	100%
products/forms.py|	20|	0	0	100%
products/models.py|	103|	16	0	84%
products/test_models.py|	14|	0	0	100%
products/test_views.py|	208|	4	0	98%
products/tests.py|	1|	0	0	100%
products/urls.py|	3|	0	0	100%
products/views.py|	288|	120	0	58%
profiles/__init__.py|	0|	0	0	100%
profiles/admin.py|	3|	0	0	100%
profiles/apps.py|	4|	0	0	100%
profiles/forms.py|	16|	9	0	44%
profiles/models.py|	21|	1	0	95%
profiles/test_views.py|	57|	57	0	0%
profiles/tests.py|	1|	1	0	0%
profiles/urls.py|	3|	0	0	100%
profiles/views.py|	31|	23	0	26%
Total|	1412|	473	0	67%
coverage.py v6.3.2, created at 2022-05-03 11:12 +0000

## Validation
All files were checked for format validation.

### CSS
The validator used to check validity of CSS code was [W3 Jigsaw](https://jigsaw.w3.org/css-validator/).

|File|Result|Status|
|----|------|------|
|base.css|||

### HTML
The validator used to check validity of HTML code was [W3C](https://validator.w3.org/).

|App|Template|Result|Status|
|---|--------|------|------|
|n/a|base.html|||
|Home|index.html|||
|Products|products.html|||
|Products|product_detail.html|||
|Products|add_product.html|||
|Products|edit_product.html|||
|Products|create_sale.html|||
|Profile|liked.html|||
|Profile|profile.html|||
|Checkout|checkout.html|||
|Checkout|checkout_success.html|||
|Bag|bag.html|||

### Javascript
The validator used to check validity of Javascript code was [JSHINT](https://jshint.com/).

|App|Template|Result|Status|
|---|--------|------|------|
|-|base.html|-|-|
|Home|index.html|-|-|
|Products|products.html|||
|Products|product_detail.html|||
|Products|add_product.html|||
|Products|edit_product.html|||
|Profile|liked.html|||
|Profile|profile.html|||
|Checkout|checkout.html|||
|Checkout|checkout_success.html|||
|Bag|bag.html|||