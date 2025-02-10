from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from tools.search_tool import SearchTool
from tools.trend_scraper_tool import TrendScraperTool
from tools.weather_forecast_tool import WeatherForecastTool
from tools.csv_reader_tool import CsvReaderTool


@CrewBase
class Inv():
    """Inv crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self, city, csv_path):
        self.city = city
        self.csv_path = csv_path  # Store CSV path

        # ✅ Initialize all tools properly
        self.search_tool = SearchTool()
        self.trend_scraper_tool = TrendScraperTool()  
        self.weather_tool = WeatherForecastTool()
        self.csv_reader_tool = CsvReaderTool(csv_path=csv_path) 
    # ------------------ Agents ------------------
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            verbose=True,
            allow_delegation=False,
            max_iter=3,
            tools=[self.search_tool, self.trend_scraper_tool, self.weather_tool],
            max_rpm=20
        )

    @agent
    def reporting_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['reporting_analyst'],
            verbose=True,
            allow_delegation=False,
            max_iter=3,
            tools=[self.search_tool, self.trend_scraper_tool, self.weather_tool],
            max_rpm=20
        )

    @agent
    def inventory_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['inventory_analyst'],
            verbose=True,
            allow_delegation=False,
            max_iter=3,
            max_rpm=20
        )

    # ------------------ Tasks ------------------
    @task
    def research_weather_task(self) -> Task:
        return Task(config=self.tasks_config['research_weather_task'],tools=[self.search_tool, self.trend_scraper_tool, self.weather_tool])

    @task
    def research_trends_task(self) -> Task:
        return Task(config=self.tasks_config['research_trends_task'],tools=[self.search_tool, self.trend_scraper_tool, self.weather_tool])

    @task
    def research_events_task(self) -> Task:
        return Task(config=self.tasks_config['research_events_task'],tools=[self.search_tool, self.trend_scraper_tool, self.weather_tool])

    # ------------------ Analysis Tasks ------------------
    @task
    def analysis_product_trends_task(self) -> Task:
        return Task(config=self.tasks_config['analysis_product_trends_task'],tools=[self.search_tool, self.trend_scraper_tool, self.weather_tool])

    @task
    def analysis_size_forecast_task(self) -> Task:
        return Task(config=self.tasks_config['analysis_size_forecast_task'],tools=[self.search_tool, self.trend_scraper_tool, self.weather_tool])

    # ------------------ Optimization Tasks ------------------

    
    @task
    def optimization_inventory_task(self) -> Task:
        return Task(config=self.tasks_config['optimization_inventory_task'],tools=[self.csv_reader_tool])

    @task
    def optimization_production_plan_task(self) -> Task:
        return Task(
            config=self.tasks_config['optimization_production_plan_task'],
            output_file="final.md"
        )


    # ------------------ Crew Assembly ------------------
    @crew
    def crew(self) -> Crew:
        """Creates the Inv crew"""
        return Crew(
            agents=self.agents,   # Automatically created by the @agent decorator
            tasks=self.tasks,     # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # Uncomment if you wish to use hierarchical processing
        )
