Testing

I carried out testing on all elements and pages on the Saoirse's Burgers website.


#### Navbar
The Navbar has links for Home, About, Menu, Events, Chefs, Contact, Register, Login and Book A Table

#### Navbar
| Testing | Steps | Expected Result | Result |  
| - | - | - | - |
| Navbar | Check that each link brings the user to the correct section of the site | User is brought to the correct section of the site | PASS |

#### Hero Section
| Testing | Steps | Expected Result | Result | 
| - | - | - | - |
| Book a Table Button | Click the Book a Table Button | User will be brought to the Book Page | PASS |

#### Menu Section
| Testing | Steps | Expected Result | Result | 
| - | - | - | - |
| Burgers Link | Click the Burgers Link | User will be shown the menu for Burgers | PASS |
| Fries Link | Click the Fries Link | User will be shown the menu for Fries | PASS |
| Drinks Link | Click the Drinks Link | User will be shown the menu for Drinks | PASS |
| Desserts Link | Click the Desserts Link | User will be shown the menu for Desserts | PASS |

#### Footer
| Testing | Steps | Expected Result | Result | 
| - | - | - | - |
| Twitter Link | Click the Twitter Link | Twitter Homepage will open in a new tab | PASS |
| Facebook Link | Click the Facebook Link | Facebook Homepage will open in a new tab | PASS |
| Instagram Link | Click the Instagram Link | Instagram Homepage will open in a new tab | PASS |

#### Register
| Testing | Steps | Expected Result | Result | 
| - | - | - | - |
| Register Link in NavBar | Click the Register Link | User will be taken to the Sign Up Page and see the sign up form | PASS |
| Username Field - Form Validation | Leave username empty | User will be prompted to enter a username | PASS |
| Password Field - Form Validation | Enter invalid password | User will be prompted to enter a unique password, at least 8 characters long | PASS |
| Password (again) Field - Form Validation| Enter invalid, different password | User will be prompted to enter the matching password | PASS |
| Submit Form | Fill in all fields correctly | Message appears 'Successfully signed in as < Username >' | PASS |

#### Booking Page
| Testing | Steps | Expected Result | Result | 
| - | - | - | - |
| Book a Table Button in NavBar | Click the Book a Table Button | User will be taken to the Booking page and will see the booking form form | PASS |
| Name Field - Form Validation | Leave Name empty | User will be prompted to enter a Name | PASS |
| Email Address Field - Form Validation | Leave email address empty | User will be prompted to enter an email address | PASS |
| Phone Number Field - Form Validation | Leave phone number empty | User will be prompted to enter a phone number | PASS |
| Date Field - Form Validation | Leave date empty | User will be prompted to enter a date | PASS |
| Time Field - Form Validation | Leave time empty | User will be prompted to enter a time | PASS |
| Number of Guests Field - Form Validation | Leave number of guests | User will be prompted to enter the number of guests | PASS |
| Special Occasion - Form Validation | Leave Special Occasion empty | User will be prompted to an occasion from the dropdown menu | PASS |
| Submit Form | Fill in all fields correctly | Message appears 'Booking Confirmed' | PASS |

#### My Bookings
| Testing | Steps | Expected Result | Result | 
| - | - | - | - |
| My Bookings Link in NavBar | Click My Bookings Link | User will be taken to the My Bookings Page | PASS |
| Bookings Appear | Submit successful booking | On successful booking, the booking will appear in the My Bookings Page | PASS |
| Bookings Are Editable | Click Edit Button | User will be shown their booking form with editable fields | PASS |
| Edit Booking - Submit Changes | Update any of the fields and click Submit button | User will see a message saying 'Your booking has been updated' and will be redirected to the My Bookings Page | PASS |
| Delete Booking - Submit Changes | Click Delete button | User will be redirected to the home page and see a message 'Your booking has been cancelled' | PASS |

#### Logout
| Testing | Steps | Expected Result | Result | 
| - | - | - | - |
| Logout Link in Navbar when user is signed in | Click the Logout Link | User will be taken to the Sign Out Page | PASS |
| Sign Out Button | Click Sign Out Button | User will be redirected to the home page and will see a message 'You have been signed out' | PASS |
