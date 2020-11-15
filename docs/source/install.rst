Getting Started
======================================

Installation
-----------------

To install run:

``pip install skingrabber``

or

``pip3 install skingrabber``


Some examples are provided on `GitHub <https://github.com/MylesMor/hypixelapi/tree/master/examples>`_.


Examples
-----------------


.. code-block:: python
  :linenos:

  from skingrabber import skingrabber

  sg = skingrabber()

  response = sg.get_skin(user='username')
  print(response)

.. code-block:: python
  :linenos:

  from skingrabber import skingrabber

  sg = skingrabber()

  response = sg.get_uuid(user='username')
  print(response)

.. code-block:: python
  :linenos:

  from skingrabber import skingrabber

  sg = skingrabber()

  response = sg.get_skin_rendered(user="emirsurmen")
  print(response)