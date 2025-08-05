##  Project: Movie Recommender System Using Machine Learning!

![6 (1)](https://github.com/user-attachments/assets/3b45a973-6698-463f-97d7-f78b08aab0b9)

## Why Recommendation Systems?

Recommendation systems are becoming increasingly important in today’s extremely busy world. People are always short on time with the myriad tasks they need to accomplish in the limited 24 hours. Therefore, recommendation systems are important as they help them make the right choices, without having to expend their cognitive resources.

The purpose of a recommendation system basically is to search for content that would be interesting to an individual. Moreover, it involves a number of factors to create personalised lists of useful and interesting content specific to each user/individual. Recommendation systems are Artificial Intelligence based algorithms that skim through all possible options and create a customized list of items that are interesting and relevant to an individual. These results are based on their profile, search/browsing history, what other people with similar traits/demographics are watching, and how likely are you to watch those movies. This is achieved through predictive modeling and heuristics with the data available.

## Types of Recommendation System :

##  1) Content-Based Recommendation


Content-based systems, which use characteristic information and takes item attriubutes into consideration .

Twitter , Youtube .

Which music you are listening , what singer are you watching . Form embeddings for the features .

User specific actions or similar items reccomendation .

It will create a vector of it .

These systems make recommendations using a user's item and profile features. They hypothesize that if a user was interested in an item in the past, they will once again be interested in it in the future

One issue that arises is making obvious recommendations because of excessive specialization (user A is only interested in categories B, C, and D, and the system is not able to recommend items outside those categories, even though they could be interesting to them).

 ## 2 ) Collaborative Based :
Collaborative filtering systems, which are based on user-item interactions.

Clusters of users with same ratings , similar users .

Book recommendation , so use cluster mechanism .

We take only one parameter , ratings or comments .

In short, collaborative filtering systems are based on the assumption that if a user likes item A and another user likes the same item A as well as another item, item B, the first user could also be interested in
the second item .

Issues are :

User-Item nXn matrix , so computationally expensive .

Only famous items will get reccomended .

## About this project:

## Demo

<img width="1366" height="706" alt="m" src="https://github.com/user-attachments/assets/426aa3a6-1ef4-40c3-bb08-0b790f94ad52" />

<img width="1366" height="706" alt="m2" src="https://github.com/user-attachments/assets/7563aa2a-41a0-4bb2-9af3-f828cd351f65" />

<img width="1366" height="709" alt="m3" src="https://github.com/user-attachments/assets/6175c179-5374-43a8-8b69-1f77ec00c68b" />



### 📊 Dataset Used
- [TMDB Movie Metadata – Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

### 🧠 Concept Behind the Model (`model.pkl`)
- This project uses **Cosine Similarity**, a metric to measure how similar two vectors (movies) are based on their content.
1. Cosine Similarity compares vector angles rather than magnitudes.
2. Movie metadata (like genre, keywords, cast) is converted into **numerical vectors** using techniques like `CountVectorizer`.
3. The cosine similarity score is computed between movies, resulting in a value between **0 and 1**:
   - `0` = completely different
   - `1` = completely similar

---

### 🛠️ How to Run the Project

#### 📦 Step 1: Clone the Repository
```bash
git clone https://github.com/entbappy/Movie-Recommender-System-Using-Machine-Learning.git
cd Movie-Recommender-System-Using-Machine-Learning

#### Step 2: Create & Activate a Conda Environment
bash
Copy code
conda create -n movie python=3.7.10 -y
conda activate movie

#### 📥 Step 3: Install Required Dependencies
bash
Copy code
pip install -r requirements.txt
#### ⚙️ Step 4: Run the Main Script to Generate the Model
bash
Copy code
python app.py
