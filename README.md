# E-COMMERCE WEBSITE 


## eCommerce Admin Dashboard - Portfolio Project

As part of my portfolio, I developed an exciting eCommerce web application with a user-friendly and secure admin view. This admin dashboard empowers administrators to efficiently manage various aspects of the eCommerce platform, ensuring a seamless experience for users. Let me walk you through the key highlights:

##  Features:

### Centralized Control Center:
The admin dashboard serves as the central control center for authorized administrators. It provides an organized overview of all products available on the platform, enabling administrators to manage them effortlessly.

### Brand and Category Management:
The platform offers a diverse range of brands and product categories. With the brand and category management feature, administrators can easily view, organize, and update brand and category information. This ensures the products are well-structured for customers' convenience.

### User Registration and Login:
The admin view includes secure user registration and login functionalities. New users can sign up easily, and their passwords are encrypted for enhanced security. Returning users can log in with confidence, knowing their credentials are protected.

### *Screenshot of a new user registering.*
![User Register](https://github.com/Mumin8/e-commerce-website-python/blob/main/screenshots/register.PNG)
If the user provided the right registration data, the registration will be successful

### *Screenshot of the user login with wrong credentials.*
![User Login](https://github.com/Mumin8/e-commerce-website-python/blob/main/screenshots/wrong_login.PNG)
If the user's credentials are correct login will be allowed otherwise it will be disallowed


## Value Proposition:

### Empowering Administrators:
The admin view empowers administrators to efficiently manage the platform without the need for technical assistance. They can focus on curating an engaging shopping experience for customers, streamlining brand and category information with ease.

### *Screenshot of the admin logged in with the correct credentials*
![Admin Dashboard](https://github.com/Mumin8/e-commerce-website-python/blob/main/screenshots/admin_page.PNG)
If the user is the admin, he will get to the admin page where he/she will be able to manage the products

### Seamless User Experience:
A well-organized admin view translates to a well-structured shopping experience for the users. Customers can easily find products and navigate through various categories, enhancing their overall satisfaction.

### Security First Approach:
I prioritized security in this project. User passwords are securely encrypted, ensuring that sensitive information remains safe even in the event of a data breach.

## Shopping Cart Functionality:
The eCommerce web application provides a user-friendly shopping cart feature, allowing customers to add products to their cart and keep track of their selected items. Let's explore how it works:

### Adding Products to Cart
#### Add to Cart Button:
On each product page, customers can find an "Add to Cart" button. When they click this button, it triggers the AddCart function

#### Handling Cart Data:
The AddCart function processes the data from the product page, such as the product ID, quantity, and selected color. It retrieves the product details from the database and constructs a dictionary with the relevant information

#### Cart Session:
To keep track of the cart items across multiple pages, we use a session called "Shoppingcart." If the session already exists, the new product information is added to it. If not, a new session is created with the product data

### Viewing the Shopping Cart
#### Cart Icon:
We provide a cart icon in the navigation bar, allowing customers to view their shopping cart at any time.

#### The getCart Function:
The getCart function retrieves the cart data from the "Shoppingcart" session. It calculates the subtotal, applies any available discounts, calculates taxes, and determines the grand total.

### Cart Information Display
#### Home page
![Shop Home Page](https://github.com/Mumin8/e-commerce-website-python/blob/main/screenshots/home_page.PNG)
#### Cart Page:
When customers navigate to the shopping cart page, they can see a summary of their selected products, including product names, prices, quantities, and colors.
![User Cart items](https://github.com/Mumin8/e-commerce-website-python/blob/main/screenshots/detailsAndCart.PNG)

#### Subtotal, Discounts, and Taxes:
The cart page displays the subtotal of all selected items, taking into account any available discounts. It also calculates the applicable taxes (6%) for the order.
![The details in Cart](https://github.com/Mumin8/e-commerce-website-python/blob/main/screenshots/cart_details.PNG)

#### Grand Total:
The cart page shows the final grand total, which includes the subtotal and taxes.

With the shopping cart functionality, customers can easily add products to their cart and keep track of their selections throughout their shopping journey. The cart page provides a transparent view of the order details, making the checkout process smooth and enjoyable for the users.
![Shopping Cart](https://github.com/Mumin8/e-commerce-website-python/blob/main/screenshots/detailsAndCart1.PNG)
