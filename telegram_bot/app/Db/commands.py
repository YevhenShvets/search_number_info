from .connect import *
import datetime


def select_number_info(number):
    cur = conn.cursor()
    cur.execute('SELECT n.id, n.number, na.last_view_date, na.views FROM "number" as n '
                'INNER JOIN "number_activity" as na ON n.id = na.id_number WHERE n.number = %s', (number,))

    number_info = cur.fetchone()
    cur.close()
    if not number_info:
        insert_number(number)
        return select_number_info(number)
    return number_info


def update_number_activity(number_id):
    last_date = datetime.datetime.now()
    cur = conn.cursor()
    cur.execute('UPDATE "number_activity" SET views=views+1, last_view_date=%s WHERE id_number=%s;',
                (last_date, number_id))
    conn.commit()
    cur.close()


def insert_comment(data):
    date_c = datetime.datetime.now()
    cur = conn.cursor()
    cur.execute('INSERT INTO "comment"(id_number, content, date_create, level) VALUES(%s, %s, %s, %s) RETURNING id',
                (data['number_id'], data['comment'], date_c, data['level_id']))
    id_ = cur.fetchone()[0]
    conn.commit()
    insert_comment_activity(id_)
    cur.close()


def select_comment(number_id, offset):
    cur = conn.cursor()
    cur.execute('SELECT c.id_number, c.content, c.date_create, c.level, c.id, ca.good, ca.bad FROM "comment" as c '
                'LEFT JOIN "comment_activity" as ca ON c.id=ca.id_comment '
                'WHERE c.id_number=%s ORDER BY c.date_create LIMIT 1 OFFSET %s', (number_id, offset))

    comment = cur.fetchone()
    cur.close()
    return comment


def select_comment_len(number_id):
    cur = conn.cursor()
    cur.execute('SELECT COUNT(c.id) FROM comment as c WHERE c.id_number=%s', (number_id,))

    comment_count = cur.fetchone()[0]
    cur.close()
    return comment_count


# private
def insert_number(number):
    date_added = datetime.datetime.now()
    cur = conn.cursor()
    cur.execute('INSERT INTO "number"(number, date_added, is_active) VALUES(%s, %s, %s) RETURNING id',
                (number, date_added, True))
    id_ = cur.fetchone()[0]
    conn.commit()
    insert_number_activity(id_, date_added)
    cur.close()


# private
def insert_number_activity(number_id, date_added):
    cur = conn.cursor()
    cur.execute('INSERT INTO "number_activity"(id_number, last_view_date, views) VALUES(%s, %s, %s)',
                (number_id, date_added, 0))
    conn.commit()
    cur.close()


# private
def insert_comment_activity(comment_id):
    cur = conn.cursor()
    cur.execute('INSERT INTO "comment_activity"(id_comment, good, bad) VALUES(%s, 0, 0)',
                (comment_id,))
    conn.commit()
    cur.close()
