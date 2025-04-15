Run API server on local:
cd to API path and run as below.
python main.py

Different API end points:

1.http://127.0.0.1:5000/welcome
2.http://127.0.0.1:5000/liveness
3.http://127.0.0.1:5000/recommend?title=A%20Walk%20to%20Remember

API response for /recommend end point:
{
  "recommendations": [
    [
      "The Rescue",
      "Nicholas Sparks",
      "http://images.amazon.com/images/P/0446610399.01.MZZZZZZZ.jpg"
    ],
    [
      "The Notebook",
      "Nicholas Sparks",
      "http://images.amazon.com/images/P/0446605239.01.MZZZZZZZ.jpg"
    ],
    [
      "A Bend in the Road",
      "Nicholas Sparks",
      "http://images.amazon.com/images/P/0446527785.01.MZZZZZZZ.jpg"
    ],
    [
      "The Reptile Room (A Series of Unfortunate Events, Book 2)",
      "Lemony Snicket",
      "http://images.amazon.com/images/P/0064407675.01.MZZZZZZZ.jpg"
    ],
    [
      "Nights in Rodanthe",
      "Nicholas Sparks",
      "http://images.amazon.com/images/P/0446531332.01.MZZZZZZZ.jpg"
    ]
  ]
}


#Deploy streamlit app
cd UI
python -m streamlit run app.py
