# Yommies 

*"Pick 'N' mix made easy"*

Yommies is a pick 'n' mix delivery service. Just pick a selection of your favourite sweets and have them delivered to your doorstep in a matter of clicks.

---

# Contents
1. [UX / Project Goals](#ux)
2. [User Stories](#user-stories)
3. [Site Owner Goals](#site-owner-goals)
4. [Design Choices](#design-choices)
5. [Wireframes](#wireframes)
6. [Features & Potential Future features](#features)
7. [Technologies used](#languages)
8. [Testing](#testing)
9. [Issues and resolutions](#issues-and-resolutions)
10. [Deployment](#deployment)
11. [Credits](#credits)
---

## UX


### Project Goals

Create a responsive web app with the django framework where users can build their own selection of pick n mix sweets, securely pay and have them delivered.


#### User stories

* *"As a user of the site I'd like to be able to use this service on my mobile, tablet or desktop"*
* *"As a shopper I'd like to be able to build my own bag online and have them delivered to my house"*
* *"As a shopper I'd like the option to order pick 'N' mix bags with pre-selected contents"*
* *"As a shopper I'd like to have a wide variety of sweets to choose from and see pictures of what they look like"*
* *"As a user of the site I'd like to be able to have an account and save my details to make future transactions easier and faster"*
* *"As a site user I'd like to recieve email notification that my account has been set up properly"*
* *"As a user of the site I want it to be easy and intuitive to navigate"*
* *"As a shopper I want to see what's in my bag at checkout and how much I'm paying altogher"*
* *"As a shopper I want the assurance my details are safe and that payment is done securely"*
* *"As a shopper I'd like to receive email confirmation about my order"*
* *"As a site-owner I want to be able to add, edit or delete products via a management interface"*

#### Site Owner Goals

* Provide users a service to build their own pick n mix selections or chooce ready made bags which are then delivered to them pending successful payment.
* The ability to manage products, stock levels and prices via user friendly admin section.

---

## Design Choices

* Brand and headings font - [Cabin Sketch](https://fonts.google.com/specimen/Cabin+Sketch?category=Display&preview.text=Yommies&preview.text_type=custom#about)
* All other fonts [Comfortaa](https://fonts.google.com/specimen/Comfortaa?category=Display&preview.text=Yommies&preview.text_type=custom&selection.family=Comfortaa:wght@300;400;500;600;700#about) and [Roboto](https://fonts.google.com/specimen/Roboto?query=roboto#about)
* Kawaii star flat style icons from [flaticons](https://www.flaticon.com/packs/sweets-4?word=sweets&k=1606073810222)
* Soft pastel colours to compliment the kawaii icons and sweet theme
    * #F4FFB4 - lemon yellow crayon
    * #FFEECE - blanched almond
    * #FFE5B4 - peach
    * #FFC0B4 - melon
    * #E5B4FF - mauve
    * #4D4C7D - purple navy
    * #C0B4FF - maximum blue purple
    * #B4CEFF - baby blue eyes
    * #EBF1FF - magnolia
    * #B4F4FF - blizzard blue
    * #B4FFE5 - aero blue
    * #FFFFFF - white

---

### Wireframes

I used [Balsamiq](https://balsamiq.com/) to create wireframes for **mobile, tablet and desktop.**

You can find my wireframes [here](https://github.com/AlexPullen91/yommies/tree/master/wireframes).

---

### Features

* Build your own pick 'N' mix - select 10 scoops of your choice to make up a 1KG bag of pick 'N' mix.
* Option to choose a pre-selected bag of Fizzy only, Jelly only, Chocolate only, Vegetarian only or a random selection.
* User accounts - sign up and login when ordering to save personal details to speed up future checkouts.
* Shopping bag and checkout with stripe payments.
* Fixed navbar for speedy navigation and constant view of shopping bag total.
    * Collapsible on smaller screens
* Footer with social links, more site navigation, about, T&C's etc.

#### Potential Future features

* Reviews
* More product bundles - merchandise etc.

---

## Technologies Used

### Languages

* [HTML](https://en.wikipedia.org/wiki/HTML)
* [CSS](https://en.wikipedia.org/wiki/CSS)
* [JavaScript](https://www.javascript.com/)
* [Python](https://www.python.org/)

---

### Libraries

* [Django](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
* [Bootstrap](https://getbootstrap.com/)
* [jQuery](https://jquery.com/)
* [Google Fonts](https://fonts.google.com/)

---

### Tools

* [Github](https://github.com/)
* [Gitpod](https://www.gitpod.io/)
* [Git](https://git-scm.com/)
* [Google Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
* [Balsamiq](Balsamiq)

---

## Testing

Testing for responsiveness and bugs throughout development was carried out with google chrome developer tools and the device toolbar to ensure compatibility on all screen sizes.

HTML ran through [W3 validator](https://validator.w3.org/)

CSS ran through [W3 validator](https://jigsaw.w3.org/css-validator/)
* Everything good except some warnings related to webkits and bootstrap css

Python ran through [PEP8 online check](http://pep8online.com/)
* Everything good except for some long lines that break code if altered.

## Manual Testing

Yommies was tested manually. This involved step by step processes going through all the apps functionality and testing features such as form validation. Some examples are detailes below.

*Test case:* **User sign up process**

This test determines if the user sign up process works as intended

    1. User clicks register button under profile icon dropdown menu and is directed to sign up page.
    2. Clicking sign up button at bottom of form alerts user to empty required input fields.
    3. Entering an email in email field or user name in user name field that is taken fails the process and notifies the user.
    4. Entering a unique email and name in email and username field with passwords that do not match alerts user to try again.
    5. Entering a unique email and name in email and username field with matching passwords successfully creates a new user and directs them to landing page.

    Verdict: Working as intended

*Test case:* **User login process**

This test determines if the user login process works as intended

    1. User clicks signin button under profile icon dropdown menu and is directed to login page.
    2. Clicking login button at bottom of form alerts user to empty required input fields.
    3. Entering a name into username/email field and a password into password field that aren't in the database alerts user with an error message.
    4. Entering a name into username/email field that is saved in the database and entering an incorrect password alerts user with an error message.
    5. Entering a name into username field that is saved in the database along with entering the correct password redirects user to landing page.

    Verdict: Working as intended

*Test case:* **Adding scoops to bag**

This test determines if the add scoops to bag works as intended 

    1. User clicks build on landing page or navbar and is directed to scoops page.
    2. Clicking add scoops or checkout alerts user to select an item from missing input fields.
    3. Selecting 10 scoops of any order or quantity and then clicking add scoops notifies user they have been added to the cart.
    4. Clicking go to checkout takes user to checkout page to complete purchase.
    5. Click return takes user back to landing page.

    Verdict: Working as intended - same process applied to add to bags.

*Test case:* **Shopping Cart**

This test determines if the shopping cart feature works as intended 

    1. Once users have selected bags or scoops they are directed to their cart with all their selections.
    2. Adjusting quantity with minus and plus arrows and then clicking update sets quantity to new value - grand total reflects this.
    3. Clicking remove all removes item from the cart entirely - grand total reflects this.
    4. Clicking checkout takes user to payment section.

    Verdict: Working as intended

*Test case:* **Checkout**

This test determines if the checkout feature works as intended 

    1. Clicking checkout from the cart page takes user to payment form.
    2. Clicking complete order before filling in all required fields alerts user to do so.
    3. Clicking complete order with required fields filled in but no card details alerts user it's incomplete.
    4. Clicking complete order with required fields filled in and valid card details results in success message and user shown order information.
    5. If user is registered and logged in then ticking the save info box saves their information for next time.
    6. Clicking adjust bag takes user back to cart page.

    Verdict: Working as intended

### Issues and Resolutions



---

## Deployment


### Local Deployment


### Heroku Deployment


## Credits

* Favicon from [favicon generator](https://www.favicon.cc/?)

### Content


### Code


### Acknowledgements


### Disclaimer

*This site is intended for educational purposes only.*