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

      ;

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

;