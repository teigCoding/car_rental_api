from neo4j import GraphDatabase
#hello
class Neo4jService:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_car(self, car_data):
        with self.driver.session() as session:
            result = session.run(
                "CREATE (c:Car {make: $make, model: $model, year: $year, status: $status}) RETURN c",
                make=car_data["make"],
                model=car_data["model"],
                year=car_data["year"],
                status=car_data.get("status", "available")
            )
            return result.single()["c"]

    def get_all_cars(self):
        with self.driver.session() as session:
            result = session.run("MATCH (c:Car) RETURN c")
            return [record["c"] for record in result]
        
    def get_car_by_id(self, car_id):
        with self.driver.session() as session:
            result = session.run("MATCH (c:Car) WHERE ID(c) = $car_id RETURN c", car_id=car_id)
            record = result.single()
            return record["c"] if record else None
