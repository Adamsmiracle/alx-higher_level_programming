--- Creates database and create user then gives the user only select privilege
CREATE DATABASE hbtn_0d_2;
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
GRANTS SELECT ON hbtn_0d_2 TO user_0d_2@localhost;