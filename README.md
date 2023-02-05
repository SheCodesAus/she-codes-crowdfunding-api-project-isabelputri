# {{ Bring Joy to the Feline Friends of Kitty Cat Island: Tsunami Relief Fund }}

{{ "Meow! Help! Emergency on Kitty Cat Island! Tsunami has struck and many of our homes have been destroyed. We need your help to rebuild and care for all of our feline friends. Please donate what you can, every little bit helps. We need funds to provide food, shelter, and medical care. Thank you for your kindness and generosity. Together, we can make Kitty Cat Island a safe and comfortable place for all of us cats. Purr-lease help! Meow!" }}

Target audience: Resident, friends and families, cat lovers - Australia and beyond

Submission file: https://docs.google.com/document/d/1kc9b_IF-FPE1cbPPRf9WNz-HhDhWmkKU55lK-IIR5TE/edit?usp=sharing/
## Features

### User Accounts

- [X] Username
- [X] Email Address
- [X] Password

### Project

- [X] Create a project
  - [X] Title
  - [X] Owner (a user)
  - [X] Description
  - [X] Image
  - [X] Target Amount to Fundraise
  - [X] Open/Close (Accepting new supporters)
  - [X] When was the project created
- [X] Ability to pledge to a project
  - [X] An amount
  - [X] The project the pledge is for
  - [X] The supporter
  - [X] Whether the pledge is anonymous
  - [X] A comment to go with the pledge
  
### Implement suitable update delete

**Note: Not all of these may be required for your project, if you have not included one of these please justify why.**

- Project
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [X] Destroy
- Pledge
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [X] Destroy
- User
  - [X] Create
  - [X] Retrieve
  - [X] Update
  - [X] Destroy

### Implement suitable permissions

**Note: Not all of these may be required for your project, if you have not included one of these please justify why.**

- Project
  - [x] Limit who can create
  - [ ] Limit who can retrieve --> for transparency purposes, anyone should be able to view all projects
  - [x] Limit who can update
  - [x] Limit who can delete
- Pledge
  - [x] Limit who can create
  - [ ] Limit who can retrieve --> for transparency purposes, anyone should be able to view all pledges
  - [x] Limit who can update
  - [x] Limit who can delete
- User
  - [ ] Limit who can retrieve --> for transparency purposes, anyone should be able to view all users
  - [x] Limit who can update
  - [x] Limit who can delete

### Implement relevant status codes

- [x] Get returns 200
- [x] Create returns 201
- [x] Not found returns 404

### Handle failed requests gracefully 

- [x] 404 response returns JSON rather than text

### Use token authentication

- [X] implement /api-token-auth/

## Additional features

- [X] {Change password}

{{ Any logged in user will be able to change their account's password }}

- [X] {Title Feature 2}

{{ description of feature 2 }}

- [ ] {Title Feature 3}

{{ description of feature 3 }}

### External libraries used

- [ ] django-filter


## Part A Submission

- [X] A link to the deployed project. (small-smoke-3626.fly.dev/)
- [X] A screenshot of Insomnia, demonstrating a successful GET method for any endpoint.
- [X] A screenshot of Insomnia, demonstrating a successful POST method for any endpoint.
- [X] A screenshot of Insomnia, demonstrating a token being returned.
- [X] Your refined API specification and Database Schema.

### Step by step instructions for how to register a new user and create a new project (i.e. endpoints and body data).

1. Create User

```shell
curl --request POST \
  --url http://localhost:8000/users/ \
  --header 'Content-Type: application/json' \
  --data '    {
        "email": "test2@test.com",
        "username": "test2",
        "password": "test2"
    }'
```

2. Sign in User

```shell
curl --request POST \
  --url http://localhost:8000/api-token-auth/ \
  --header 'Content-Type: application/json' \
  --data '{
  "username":"test",
  "password": "test"
}'
```

3. Create Project

```shell
curl --request POST \
  --url http://localhost:8000/projects/ \
  --header 'Authorization: Token d937ed9164712ae30c4ec4ff1d492839c1f53c00' \
  --header 'Content-Type: application/json' \
  --data '{
	"id": 1,
	"title": "Help the Feline Friends of Kitty Cat Island: Tsunami Relief Fund",
	"description": "Purr-lease consider donating to provide food, shelter, and medical aid to the feline friends affected by this tragedy",
	"goal": 100,
	"image": "https://upload.wikimedia.org/wikipedia/commons/c/c1/Dollar_bill_and_small_change.jpg",
	"is_open": true,
	"date_created": "2023-02-04T15:40:05.260980Z"
}'
```