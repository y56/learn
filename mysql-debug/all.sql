SELECT 
  ERR.Created, 
  ERR.create_date, 
  ERR.Error, 
  REC.create_hour as rec_hour, 
  ERR.Id2 as err_Id, 
  REC.Id2 as rec_Id 
from 
  (
    select 
      * 
    from 
      (
        select 
          substr(Created, 1, 10) as create_date, 
          cast(substr(Created, 12, 2) as dec) as create_hour, 
          Created, 
          @tmp_Error := Error Error,
          
          cast(Id1 as dec) as Id2, 

          -- MySQL engine 8.0以後才有row_number() 我們現在是5.7.33
          -- see: https://www.mysqltutorial.org/mysql-row_number/

          -- row_number() over(partition by Error order by Id2) row_id, 
          

          @row_id := CASE  -- if `Error` (or the col you want to partition) changes, reset row_id to 1, else row_id++
            WHEN @tmp_Error = Error 
            THEN @row_id + 1 
            ELSE 1 
          END AS row_id, 

          Status 
        from 
          `checks_ddspasyntheticsalerts`, 
          (SELECT @tmp_Error := 0, @row_id := 0) as a 
        order by 
          cast(Id1 as dec)
      ) a 
    where 
      Status = 'error'
  ) ERR 

  left join 
  (
    select 
      * 
    from 
      (
        select 
          substr(Created, 1, 10) as create_date, 
          cast(
            substr(Created, 12, 2) as dec
          ) as create_hour, 
          Created, 
          @tmp_Error := Error Error,
          cast(Id1 as dec) as Id2, 

          @row_id := CASE
            WHEN @tmp_Error = Error 
            THEN @row_id + 1 
            ELSE 1 
          END AS row_id, 

          Status 
        from 
          `checks_ddspasyntheticsalerts`,
          (SELECT @tmp_Error := 0, @row_id := 0) as a
        order by 
          cast(Id1 as dec)
      ) a 
    where 
      Status = 'recovery'
  ) REC 
  on ERR.create_date = REC.create_date 
  AND ERR.Error = REC.Error 
  AND ERR.row_id = REC.row_id - 1
