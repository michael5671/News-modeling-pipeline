Ingesting Vietnamese news articles from VnExpress RSS feeds, storing them in PostgreSQL, and performing topic modeling using BERTopic for trend analysis and insights.

Tech Stack: 
| Workflow Orchestration: Apache Airflow 
| Containerization: Docker Compose 
| Database: PostgreSQL 
| NLP: Python, BERTopic, Transformers 
| Visualization: Plotly, Jupyter Notebook 

news_modeling_pipeline/
├── dags/
│ └── vnexpress_rss_dag.py # Airflow DAG for crawling RSS feeds
├── scripts/
│ └── crawl_vnexpress_rss.py # Script to crawl multi-category RSS feeds
├── notebooks/
│ └── topic_modeling_bertopic.ipynb # Jupyter Notebook for BERTopic analysis
├── docker-compose.yml
├── Dockerfile
└── README.md