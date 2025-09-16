try:
    import pymysql  # type: ignore
    pymysql.install_as_MySQLdb()
except Exception:
    # If driver isn't available yet, Django will raise a clearer error on DB use
    pass

