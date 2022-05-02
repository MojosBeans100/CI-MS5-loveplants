
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

Note: since performing manual testing, some minor adjustments may have been made to small styling details, which would result in slight differences between images on the deployed site and images of the site contained in this document.  It was ensured any changes did not affect the outcome of the testing.

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

|Critera|Desktop|Tablet|Mobile|Status|
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

|Critera|Desktop|Tablet|Mobile|Status|
|-----------|-------|------|------|------|
|upon navigating to the users profile, their identifying and account info is displayed|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651240664/LovePlants/Testing/US1/desktop1_cymipd.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651240664/LovePlants/Testing/US1/tablet1_dxupzx.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651240664/LovePlants/Testing/US1/mobile1_ebhzgp.jpg)|Pass|
|non authenticated users are redirected to the home page when attempted to navigated to the profile page via the URL|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651244363/LovePlants/Testing/US1/US%201.3/desktopurl_q32r22.jpg)|N/A|N/A|Pass|

Acceptance Criteria:
- [x] Users are aware how to reach the page for their personal account
- [x] Users can see relevant information about their account on their account page
- [x] Only the active user can access their account page

### 1.4
As a **site user** I can **access information of my previous orders** so that **I can see when I last ordered, how many orders I have, see the details of previous orders**

|Critera|Desktop|Tablet|Mobile|Status|
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

|Critera|Desktop|Tablet|Mobile|Status|
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

|Critera|Desktop|Tablet|Mobile|Status|
|-----------|-------|------|------|------|
|when user navigates to the products page, a list of projects are displayed|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651393182/LovePlants/Testing/US%202/2.1/desktop1_znk5tv.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651393176/LovePlants/Testing/US%202/2.1/tablet1_dqemdj.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651393176/LovePlants/Testing/US%202/2.1/mobile1_ild73b.jpg)|Pass|
|a Bootstrap card is used to identify the product with identifying information|[Desktop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651393176/LovePlants/Testing/US%202/2.1/desktop2_frirqa.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651393176/LovePlants/Testing/US%202/2.1/tablet2_kf4di0.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651393176/LovePlants/Testing/US%202/2.1/mobile2_ii5ogv.jpg)|Pass|

Acceptance Criteria:
- [x] Users can view products available to buy
- [x] Users can see a picture, product name, price for the product
- [x] Users can see how many products they are viewing

### 2.2
As a **site user** I can **use a search bar to input product details** so that **I can search for a specific product**

|Critera|Desktop|Tablet|Mobile|Status|
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

|Critera|Desktop|Tablet|Mobile|Status|
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

|Critera|Desktop|Tablet|Mobile|Status|
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

|Critera|Desktop|Tablet|Mobile|Status|
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

|Critera|Desktop|Tablet|Mobile|Status|
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

|Critera|Desktop|Tablet|Mobile|Status|
|-----------|-------|------|------|------|
|users receive a notification|[Destop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651479335/LovePlants/Testing/US%203/3.2%20/desktop12_p1wqyw.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651479334/LovePlants/Testing/US%203/3.2%20/tablet12_a83l3r.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651479334/LovePlants/Testing/US%203/3.2%20/mobile12_wyq7f2.jpg)|Pass|
|users see the contents of their shopping bag|[Destop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651479335/LovePlants/Testing/US%203/3.2%20/desktop12_p1wqyw.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651479334/LovePlants/Testing/US%203/3.2%20/tablet12_a83l3r.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651479334/LovePlants/Testing/US%203/3.2%20/mobile12_wyq7f2.jpg)|Pass|
|users can click the 'X' to dimiss the notification and continue shopping|[Destop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651479335/LovePlants/Testing/US%203/3.2%20/desktop3_hsjnnd.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651479334/LovePlants/Testing/US%203/3.2%20/tablet3_ouccyf.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651479334/LovePlants/Testing/US%203/3.2%20/mobile3_yfaq5d.jpg)|Pass|
|users see the number of items in their bag change|[Destop](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651479334/LovePlants/Testing/US%203/3.2%20/desktop4_fhemvp.jpg)|[Tablet](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651479334/LovePlants/Testing/US%203/3.2%20/tablet4_qpmxyn.jpg)|[Mobile](https://res.cloudinary.com/code-institute-mojos-beans/image/upload/v1651479334/LovePlants/Testing/US%203/3.2%20/mobile3_yfaq5d.jpg)|Pass|

Acceptance Criteria:
- [x] User received a notification that an item was added to their bag
- [x] User can see the contents of their bag
- [x] User can dismiss the notification
- [x] User can see their shopping bag contents change in the nav bar 

### 3.3
As a **site user** I can **see the total cost of my shopping bag change when I have added a product** so that **I'm aware of the running cost as I add products**

|Critera|Desktop|Tablet|Mobile|Status|
|-----------|-------|------|------|------|
||[Destop]()|[Tablet]()|[Mobile]()|Pass|

Acceptance Criteria:
- User can see the total of their shopping bag in the nav bar
- User can see the total including delivery in the bag view
- User can see subtotals for individual items in their bag
- User can see notification messages each time the bag total changes

### 3.4
As a **site user** I can **click on my shopping bag** so that **I can view a list of the products I have added**

|Critera|Desktop|Tablet|Mobile|Status|
|-----------|-------|------|------|------|
||[Destop]()|[Tablet]()|[Mobile]()|Pass|

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