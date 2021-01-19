CREATE TABLE ansan_edu_office (
    id text primary key,
    department text not null,
    position text,
    _name text,
    _charge integer not null,
    create_time text not null
);

CREATE TABLE hakhyun_student_staus (
    grade text primary key,
    num_class integer,
    num_boy integer,
    num_girl integer,
    total integer,
    create_date text
);