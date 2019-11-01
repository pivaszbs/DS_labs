![Screenshot](https://i.paste.pics/fe089c9b5d0cb11aca5cf5ba33139028.png)

<details>
  <summary>rs.config()</summary>
  
    ```{
        "_id" : "rs0",
        "version" : 1,
        "protocolVersion" : NumberLong(1),
        "writeConcernMajorityJournalDefault" : true,
        "members" : [
            {
                "_id" : 0,
                "host" : "m1:27017",
                "arbiterOnly" : false,
                "buildIndexes" : true,
                "hidden" : false,
                "priority" : 1,
                "tags" : {
                    
                },
                "slaveDelay" : NumberLong(0),
                "votes" : 1
            },
            {
                "_id" : 1,
                "host" : "m2:27017",
                "arbiterOnly" : false,
                "buildIndexes" : true,
                "hidden" : false,
                "priority" : 1,
                "tags" : {
                    
                },
                "slaveDelay" : NumberLong(0),
                "votes" : 1
            },
            {
                "_id" : 2,
                "host" : "m3:27017",
                "arbiterOnly" : false,
                "buildIndexes" : true,
                "hidden" : false,
                "priority" : 1,
                "tags" : {
                    
                },
                "slaveDelay" : NumberLong(0),
                "votes" : 1
            }
        ],
        "settings" : {
            "chainingAllowed" : true,
            "heartbeatIntervalMillis" : 2000,
            "heartbeatTimeoutSecs" : 10,
            "electionTimeoutMillis" : 10000,
            "catchUpTimeoutMillis" : -1,
            "catchUpTakeoverDelayMillis" : 30000,
            "getLastErrorModes" : {
                
            },
            "getLastErrorDefaults" : {
                "w" : 1,
                "wtimeout" : 0
            },
            "replicaSetId" : ObjectId("5dbc4c46e5cb0c5204ac5bf4")
        }
    }```
  
</details>
<details>
    <summary>rs.status()</summary>

    ```{
        "set" : "rs0",
        "date" : ISODate("2019-11-01T15:53:12.747Z"),
        "myState" : 1,
        "term" : NumberLong(2),
        "syncingTo" : "",
        "syncSourceHost" : "",
        "syncSourceId" : -1,
        "heartbeatIntervalMillis" : NumberLong(2000),
        "majorityVoteCount" : 2,
        "writeMajorityCount" : 2,
        "optimes" : {
            "lastCommittedOpTime" : {
                "ts" : Timestamp(1572623585, 1),
                "t" : NumberLong(2)
            },
            "lastCommittedWallTime" : ISODate("2019-11-01T15:53:05.442Z"),
            "readConcernMajorityOpTime" : {
                "ts" : Timestamp(1572623585, 1),
                "t" : NumberLong(2)
            },
            "readConcernMajorityWallTime" : ISODate("2019-11-01T15:53:05.442Z"),
            "appliedOpTime" : {
                "ts" : Timestamp(1572623585, 1),
                "t" : NumberLong(2)
            },
            "durableOpTime" : {
                "ts" : Timestamp(1572623585, 1),
                "t" : NumberLong(2)
            },
            "lastAppliedWallTime" : ISODate("2019-11-01T15:53:05.442Z"),
            "lastDurableWallTime" : ISODate("2019-11-01T15:53:05.442Z")
        },
        "lastStableRecoveryTimestamp" : Timestamp(1572623555, 1),
        "lastStableCheckpointTimestamp" : Timestamp(1572623555, 1),
        "electionCandidateMetrics" : {
            "lastElectionReason" : "electionTimeout",
            "lastElectionDate" : ISODate("2019-11-01T15:26:04.449Z"),
            "termAtElection" : NumberLong(2),
            "lastCommittedOpTimeAtElection" : {
                "ts" : Timestamp(1572621573, 1),
                "t" : NumberLong(1)
            },
            "lastSeenOpTimeAtElection" : {
                "ts" : Timestamp(1572621583, 1),
                "t" : NumberLong(1)
            },
            "numVotesNeeded" : 2,
            "priorityAtElection" : 1,
            "electionTimeoutMillis" : NumberLong(10000),
            "numCatchUpOps" : NumberLong(27017),
            "newTermStartDate" : ISODate("2019-11-01T15:26:05.397Z"),
            "wMajorityWriteAvailabilityDate" : ISODate("2019-11-01T15:26:06.632Z")
        },
        "members" : [
            {
                "_id" : 0,
                "name" : "m1:27017",
                "ip" : "172.31.21.28",
                "health" : 1,
                "state" : 1,
                "stateStr" : "PRIMARY",
                "uptime" : 2283,
                "optime" : {
                    "ts" : Timestamp(1572623585, 1),
                    "t" : NumberLong(2)
                },
                "optimeDate" : ISODate("2019-11-01T15:53:05Z"),
                "syncingTo" : "",
                "syncSourceHost" : "",
                "syncSourceId" : -1,
                "infoMessage" : "",
                "electionTime" : Timestamp(1572621964, 1),
                "electionDate" : ISODate("2019-11-01T15:26:04Z"),
                "configVersion" : 1,
                "self" : true,
                "lastHeartbeatMessage" : ""
            },
            {
                "_id" : 1,
                "name" : "m2:27017",
                "ip" : "172.31.21.80",
                "health" : 1,
                "state" : 2,
                "stateStr" : "SECONDARY",
                "uptime" : 1594,
                "optime" : {
                    "ts" : Timestamp(1572623585, 1),
                    "t" : NumberLong(2)
                },
                "optimeDurable" : {
                    "ts" : Timestamp(1572623585, 1),
                    "t" : NumberLong(2)
                },
                "optimeDate" : ISODate("2019-11-01T15:53:05Z"),
                "optimeDurableDate" : ISODate("2019-11-01T15:53:05Z"),
                "lastHeartbeat" : ISODate("2019-11-01T15:53:11.095Z"),
                "lastHeartbeatRecv" : ISODate("2019-11-01T15:53:12.724Z"),
                "pingMs" : NumberLong(0),
                "lastHeartbeatMessage" : "",
                "syncingTo" : "m3:27017",
                "syncSourceHost" : "m3:27017",
                "syncSourceId" : 2,
                "infoMessage" : "",
                "configVersion" : 1
            },
            {
                "_id" : 2,
                "name" : "m3:27017",
                "ip" : "172.31.32.162",
                "health" : 1,
                "state" : 2,
                "stateStr" : "SECONDARY",
                "uptime" : 1636,
                "optime" : {
                    "ts" : Timestamp(1572623585, 1),
                    "t" : NumberLong(2)
                },
                "optimeDurable" : {
                    "ts" : Timestamp(1572623585, 1),
                    "t" : NumberLong(2)
                },
                "optimeDate" : ISODate("2019-11-01T15:53:05Z"),
                "optimeDurableDate" : ISODate("2019-11-01T15:53:05Z"),
                "lastHeartbeat" : ISODate("2019-11-01T15:53:11.197Z"),
                "lastHeartbeatRecv" : ISODate("2019-11-01T15:53:11.457Z"),
                "pingMs" : NumberLong(0),
                "lastHeartbeatMessage" : "",
                "syncingTo" : "m1:27017",
                "syncSourceHost" : "m1:27017",
                "syncSourceId" : 0,
                "infoMessage" : "",
                "configVersion" : 1
            }
        ],
        "ok" : 1,
        "$clusterTime" : {
            "clusterTime" : Timestamp(1572623585, 1),
            "signature" : {
                "hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
                "keyId" : NumberLong(0)
            }
        },
        "operationTime" : Timestamp(1572623585, 1)
    }```
</details>

<details>
    <summary>rs.config()</summary>

```    {
        "_id" : "rs0",
        "version" : 1,
        "protocolVersion" : NumberLong(1),
        "writeConcernMajorityJournalDefault" : true,
        "members" : [
            {
                "_id" : 0,
                "host" : "m1:27017",
                "arbiterOnly" : false,
                "buildIndexes" : true,
                "hidden" : false,
                "priority" : 1,
                "tags" : {
                    
                },
                "slaveDelay" : NumberLong(0),
                "votes" : 1
            },
            {
                "_id" : 1,
                "host" : "m2:27017",
                "arbiterOnly" : false,
                "buildIndexes" : true,
                "hidden" : false,
                "priority" : 1,
                "tags" : {
                    
                },
                "slaveDelay" : NumberLong(0),
                "votes" : 1
            },
            {
                "_id" : 2,
                "host" : "m3:27017",
                "arbiterOnly" : false,
                "buildIndexes" : true,
                "hidden" : false,
                "priority" : 1,
                "tags" : {
                    
                },
                "slaveDelay" : NumberLong(0),
                "votes" : 1
            }
        ],
        "settings" : {
            "chainingAllowed" : true,
            "heartbeatIntervalMillis" : 2000,
            "heartbeatTimeoutSecs" : 10,
            "electionTimeoutMillis" : 10000,
            "catchUpTimeoutMillis" : -1,
            "catchUpTakeoverDelayMillis" : 30000,
            "getLastErrorModes" : {
                
            },
            "getLastErrorDefaults" : {
                "w" : 1,
                "wtimeout" : 0
            },
            "replicaSetId" : ObjectId("5dbc4c46e5cb0c5204ac5bf4")
        }
    }```
</details>

<details>
<summary>rs.status()</summary>
```    {
        "set" : "rs0",
        "date" : ISODate("2019-11-01T16:08:25.430Z"),
        "myState" : 2,
        "term" : NumberLong(2),
        "syncingTo" : "m1:27017",
        "syncSourceHost" : "m1:27017",
        "syncSourceId" : 0,
        "heartbeatIntervalMillis" : NumberLong(2000),
        "majorityVoteCount" : 2,
        "writeMajorityCount" : 2,
        "optimes" : {
            "lastCommittedOpTime" : {
                "ts" : Timestamp(1572624495, 1),
                "t" : NumberLong(2)
            },
            "lastCommittedWallTime" : ISODate("2019-11-01T16:08:15.467Z"),
            "readConcernMajorityOpTime" : {
                "ts" : Timestamp(1572624495, 1),
                "t" : NumberLong(2)
            },
            "readConcernMajorityWallTime" : ISODate("2019-11-01T16:08:15.467Z"),
            "appliedOpTime" : {
                "ts" : Timestamp(1572624495, 1),
                "t" : NumberLong(2)
            },
            "durableOpTime" : {
                "ts" : Timestamp(1572624495, 1),
                "t" : NumberLong(2)
            },
            "lastAppliedWallTime" : ISODate("2019-11-01T16:08:15.467Z"),
            "lastDurableWallTime" : ISODate("2019-11-01T16:08:15.467Z")
        },
        "lastStableRecoveryTimestamp" : Timestamp(1572624475, 1),
        "lastStableCheckpointTimestamp" : Timestamp(1572624475, 1),
        "members" : [
            {
                "_id" : 0,
                "name" : "m1:27017",
                "ip" : "172.31.21.28",
                "health" : 1,
                "state" : 1,
                "stateStr" : "PRIMARY",
                "uptime" : 2549,
                "optime" : {
                    "ts" : Timestamp(1572624495, 1),
                    "t" : NumberLong(2)
                },
                "optimeDurable" : {
                    "ts" : Timestamp(1572624495, 1),
                    "t" : NumberLong(2)
                },
                "optimeDate" : ISODate("2019-11-01T16:08:15Z"),
                "optimeDurableDate" : ISODate("2019-11-01T16:08:15Z"),
                "lastHeartbeat" : ISODate("2019-11-01T16:08:23.916Z"),
                "lastHeartbeatRecv" : ISODate("2019-11-01T16:08:23.662Z"),
                "pingMs" : NumberLong(0),
                "lastHeartbeatMessage" : "",
                "syncingTo" : "",
                "syncSourceHost" : "",
                "syncSourceId" : -1,
                "infoMessage" : "",
                "electionTime" : Timestamp(1572621964, 1),
                "electionDate" : ISODate("2019-11-01T15:26:04Z"),
                "configVersion" : 1
            },
            {
                "_id" : 1,
                "name" : "m2:27017",
                "ip" : "172.31.21.80",
                "health" : 1,
                "state" : 2,
                "stateStr" : "SECONDARY",
                "uptime" : 517,
                "optime" : {
                    "ts" : Timestamp(1572624495, 1),
                    "t" : NumberLong(2)
                },
                "optimeDurable" : {
                    "ts" : Timestamp(1572624495, 1),
                    "t" : NumberLong(2)
                },
                "optimeDate" : ISODate("2019-11-01T16:08:15Z"),
                "optimeDurableDate" : ISODate("2019-11-01T16:08:15Z"),
                "lastHeartbeat" : ISODate("2019-11-01T16:08:24.109Z"),
                "lastHeartbeatRecv" : ISODate("2019-11-01T16:08:24.621Z"),
                "pingMs" : NumberLong(0),
                "lastHeartbeatMessage" : "",
                "syncingTo" : "m3:27017",
                "syncSourceHost" : "m3:27017",
                "syncSourceId" : 2,
                "infoMessage" : "",
                "configVersion" : 1
            },
            {
                "_id" : 2,
                "name" : "m3:27017",
                "ip" : "172.31.32.162",
                "health" : 1,
                "state" : 2,
                "stateStr" : "SECONDARY",
                "uptime" : 2551,
                "optime" : {
                    "ts" : Timestamp(1572624495, 1),
                    "t" : NumberLong(2)
                },
                "optimeDate" : ISODate("2019-11-01T16:08:15Z"),
                "syncingTo" : "m1:27017",
                "syncSourceHost" : "m1:27017",
                "syncSourceId" : 0,
                "infoMessage" : "",
                "configVersion" : 1,
                "self" : true,
                "lastHeartbeatMessage" : ""
            }
        ],
        "ok" : 1,
        "$clusterTime" : {
            "clusterTime" : Timestamp(1572624495, 1),
            "signature" : {
                "hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
                "keyId" : NumberLong(0)
            }
        },
        "operationTime" : Timestamp(1572624495, 1)
    }```
</details>