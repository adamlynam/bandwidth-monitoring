SELECT SUM(in_bytes)/1024/1024,SUM(out_bytes)/1024/1024,mac FROM `log` WHERE hour(timestampadd(HOUR,-12,log_time)) > 1 AND hour(timestampadd(HOUR,-12,log_time)) < 7 GROUP BY mac

