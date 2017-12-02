#Prerequisites
* python3

 To install python3 or pip3 refer [this link](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-debian-8).

If python3 already present, just use following command:

    $ source StockExpert/StockExpertEnv/bin/activate

---

So virtual environment get activated,
Now to run project use the command:

    $ python StockExpert/StockExpert.py

---

Project will run, to see output just go to browser and visit [http://localhost:5000](http://localhost:5000)

---

###There is no need to install *requirement.txt*.

Still if want to install libraries, use following steps:

1. Install virtual environment

        $ [sudo] pip install virtualenv

 OR

        $ [sudo] pip3 install virtualenv

2. Now create vitualenvironment named `StockExpert`:

        $ virtualenv StockExpert

 To activate virtualenvironment:

        $ source bin/activate

 To deactivate virtualenvironment:

        $ deactivate

3. To install *requirement.txt*:

        $ (StockExpert) pip install -r requirement.txt


 OR

        $ (StockExpert) pip3 install -r requirement.txt

4. To run project use following command:

        $ (StockExpert) python StockExpert/StockExpert.py

 Now visit [http://localhost:5000](http://localhost:5000) on browser to check output.

---
* If only python3 in the system use `pip`
* if more than one python versions are installed, then use `pip3`
