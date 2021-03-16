CREATE TABLE "number"(
    "id" SERIAL NOT NULL,
    "number" VARCHAR(255) NOT NULL,
    "date_added" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "is_active" BOOLEAN NULL
);
ALTER TABLE
    "number" ADD PRIMARY KEY("id");
ALTER TABLE
    "number" ADD CONSTRAINT "number_number_unique" UNIQUE("number");
CREATE TABLE "comment"(
    "id" SERIAL NOT NULL,
    "id_number" INTEGER NOT NULL,
    "content" VARCHAR(255) NOT NULL,
    "date_create" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "level" INTEGER NOT NULL
);
ALTER TABLE
    "comment" ADD PRIMARY KEY("id");
CREATE TABLE "levels"(
    "id" INTEGER NOT NULL,
    "text" VARCHAR(255) NOT NULL,
    "color" VARCHAR(255) NULL
);
ALTER TABLE
    "levels" ADD PRIMARY KEY("id");
CREATE TABLE "comment_activity"(
    "id_comment" INTEGER NOT NULL,
    "good" INTEGER NOT NULL,
    "bad" INTEGER NOT NULL
);
ALTER TABLE
    "comment_activity" ADD PRIMARY KEY("id_comment");
CREATE TABLE "number_activity"(
    "id_number" INTEGER NOT NULL,
    "last_view_date" TIMESTAMP(0) WITHOUT TIME ZONE NOT NULL,
    "views" INTEGER NOT NULL
);
ALTER TABLE
    "number_activity" ADD PRIMARY KEY("id_number");
ALTER TABLE
    "comment" ADD CONSTRAINT "comment_id_number_foreign" FOREIGN KEY("id_number") REFERENCES "number"("id");
ALTER TABLE
    "comment" ADD CONSTRAINT "comment_level_foreign" FOREIGN KEY("level") REFERENCES "levels"("id");