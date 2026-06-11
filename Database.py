import psycopg

class Database:
    def __init__(self):
        try:
            self.conn = psycopg.connect(host="192.168.135.10",
                                        port="5432",
                                        dbname="obce",
                                        user="student",
                                        password="bluemonkey3")
            self.cur = self.conn.cursor()
        except psycopg.OperationalError as e:
            raise RuntimeError(f"Database connection failed: {e}")

    def search_town(self, town):

        search_term = f"%{town}%"
        query = 'SELECT obce_pob.nazev FROM obce_pob WHERE obce_pob.nazev ILIKE %s'
        self.cur.execute(query, (search_term,))
        towns = self.cur.fetchall()

        return [row[0] for row in towns]

    def get_districts(self):

        query = 'SELECT okresy.nazev FROM okresy'
        self.cur.execute(query)
        districts = self.cur.fetchall()

        return districts

    def get_district_info(self, district_id):

        query = """
                SELECT
                    okresy.nazev,
                    obce_pob.nazev,
                    obce_pob.pocet_obyvatel,
                    obce_pob.prumerny_vek
                FROM okresy
                JOIN obce_pob
                    ON obce_pob.id_okres = okresy.id_okres
                WHERE okresy.id_okres = %s;
                """
        self.cur.execute(query, (district_id,))
        district_info = self.cur.fetchall()

        return district_info

    def get_district_mean_info(self, district_id):
        query = """
                SELECT
                    SUM(obce_pob.pocet_obyvatel) OVER () AS okres_obyvatel,
                    AVG(obce_pob.prumerny_vek) OVER () AS okres_prumerny_vek,
                    SUM(obce_pob.pocet_muzi) OVER () AS okres_muzi,
                    SUM(obce_pob.pocet_zeny) OVER () AS okres_zeny
                FROM obce_pob
                WHERE okresy.id_okres = %s;
                """
        self.cur.execute(query, (district_id,))
        district_mean_info = self.cur.fetchall()

        return district_mean_info
    
    def close(self):
        self.cur.close()
        self.conn.close()