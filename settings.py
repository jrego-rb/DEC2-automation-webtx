from selenium import webdriver

defaultEnvironment = "desa"
defaultDriver = "chrome"

environments={

    "desa" : {
        "driver" : "chrome",
        "baseURL" : "localhost",
        "port" : "19001",
        "SACLogin":{
            "baseURL" : "localhost",
            "port" : "18080",
            "user": "ccopello",
            "password": "Prisma2039"
        },
        "QAPI":{
            "baseURL" : "localhost",
            "port" : "10115"
        },
        "coreTx": {
            "baseURL": "localhost",
            "port": "19000"
        },
        "forms":{
            "baseURL":"localhost",
            "port":"9006"
        },
        "database": {
            "host":"localhost",
            "port":13306,
            "user":"spsT_usr",
            "passwd":"veef8Eed",
            "db":"sps433"
        }

    },

    "local_machine" : {
        "driver" : "chrome",
        "baseURL" : "localhost",
        "port" : "30901",
        "SACLogin":{
            "baseURL" : "localhost",
            "port" : "30080",
            "user": "ccopello",
            "password": "pRISMA2034"
        },
        "QAPI":{
            "baseURL" : "localhost",
            "port" : "10115"
        },
        "coreTx": {
            "baseURL": "localhost",
            "port": "19000"
        },
        "forms":{
            "baseURL":"localhost",
            "port":"9006"
        }

    },

    "jenkins" : {
        "driver" : "headless_chrome",
        "baseURL" : "marathon-lb.infrastructure.marathon.mesos",
        "port" : "10001",
        "SACLogin":{
            "baseURL" : "marathon-lb.infrastructure.marathon.mesos",
            "port" : "10010",
            "user": "ccopello",
            "password": "Prisma2039"
        },
        "QAPI":{
            "baseURL" : "marathon-lb.infrastructure.marathon.mesos",
            "port" : "10115"
        },
        "coreTx":{
            "baseURL" : "marathon-lb.infrastructure.marathon.mesos",
            "port" : "10000"
        },
        "forms":{
            "baseURL":"marathon-lb.infrastructure.marathon.mesos",
            "port":"10116"
        },
        "database": {
            "host":"192.168.75.20",
            "port":3306,
            "user":"spsT_usr",
            "passwd":"veef8Eed",
            "db":"sps433"
        }

    }
}

