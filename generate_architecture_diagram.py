#%%
from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import User
from diagrams.onprem.ci import GithubActions
from diagrams.azure.devops import Pipelines
from diagrams.azure.compute import AppServices
from diagrams.custom import Custom

with Diagram("Project Architecture", filename="architecture", show=False) as a:
    user = User("Developer")
    commit = Edge(label="commit")
    with Cluster("Github"):
        repo = Custom("Github repo", "./images/Octocat.png")
        github_action = GithubActions("Github Action")
    with Cluster("Azure"):
        pipeline = Pipelines("DevOps Pipeline")
        deploy = Edge(label="deploy")
        app = AppServices("Web App")
    user >> commit >> repo >> github_action >> pipeline >> deploy >> app

