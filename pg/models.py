from django.db import models
import psycopg2 as ps
import pandas as pd


class PG:
    def queryset(self, query, pg_url):
        data_list = []
        with ps.connect(pg_url) as conn:
            with conn.cursor() as cur:
                cur.execute(query=query)
                rows = cur.fetchall()
                column_names = [d[0] for d in cur.description]
                for row in rows:
                    row_dict = {column_names[index]: value for (index, value) in enumerate(row)}
                    data_list.append(row_dict)
                _df = pd.DataFrame(data_list)
                return _df

    def get_all_stock(self):
        _sql = (
            "SELECT skl.item_name AS Склад, skl.id, gds.marking_goods AS Артикул, gds.item_name AS Наименование, rst.goods_id AS КодТовара,"
            # "rst.pull_date AS СрокГодности, rst.man_date AS ДатаИзготовления,gds.shelf_life AS СрокГодностиДни,rst.price AS ЦенаИзПрихода,"
            "SUM(rst.items_count) AS Количество "
            "FROM s_rt rst "
            "JOIN store.agent skl ON rst.store_id=skl.id "
            "JOIN goods_all gds ON rst.goods_id=gds.id "
            # f"WHERE rst.program_id=376 AND gds.group_id IN (SELECT id FROM goods_all WHERE group_id IN {tuple_id_group_goods}) "
            f"WHERE rst.program_id=376 "
            "GROUP BY rst.goods_id, skl.item_name, gds.item_name, gds.marking_goods, skl.id, "
            "rst.pull_date, rst.man_date, gds.shelf_life, rst.price "
            "ORDER BY skl.item_name, rst.goods_id"
        )
        _df_query = self.queryset(_sql, pg_url=None)
        return _df_query

    def get_stock_by_id_group(self, id_group):
        _sql = (
            "SELECT skl.item_name AS Склад, skl.id AS КодСклада, gds.marking_goods AS Артикул, gds.item_name AS Наименование, rst.goods_id AS КодТовара,"
            # "rst.pull_date AS СрокГодности, rst.man_date AS ДатаИзготовления,gds.shelf_life AS СрокГодностиДни,rst.price AS ЦенаИзПрихода,"
            "SUM(rst.items_count) AS Количество "
            "FROM s_rt rst "
            "JOIN store.agent skl ON rst.store_id=skl.id "
            "JOIN goods_all gds ON rst.goods_id=gds.id "
            f"WHERE rst.program_id=376 AND gds.group_id={id_group} "
            # f"WHERE rst.program_id=376 "
            "GROUP BY rst.goods_id, skl.item_name, gds.item_name, gds.marking_goods, skl.id, "
            "rst.pull_date, rst.man_date, gds.shelf_life, rst.price "
            "ORDER BY skl.item_name, rst.goods_id"
        )
        _df_query = self.queryset(_sql, pg_url=None)
        return _df_query

    def get_invoice(self, pg_url=None, start_date=None, end_date=None, limit=None, **filter_query):
        _sql = ("SELECT * "
                "FROM invoice "
                )
        _filter = None
        where = []
        # print(filter_query)
        for key, val in filter_query['filter_query'].items():
            if val:
                where.append('%s=%s' % (key, val))
        if start_date is not None:
            if end_date is not None:
                where.append(f"date_doc BETWEEN '{start_date}' AND '{end_date}'")
            else:
                where.append(f"date_doc > '{start_date}'")
        elif end_date is not None:
            where.append("date_doc < '%s'" % end_date)
        if len(where) > 0:
            _filter = "WHERE " + " AND ".join(where)
        if limit:
            _filter += " LIMIT " + str(limit)
        if _filter:
            _sql += _filter
        else:
            _sql += "LIMIT 5"
        _df_query = self.queryset(_sql, pg_url=pg_url)
        # _df_query = pd.DataFrame()
        return _df_query
