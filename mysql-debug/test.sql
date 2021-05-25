set @row_id_ERR := 0;

select
          substr(Created, 1, 10) as create_date, 
          cast(substr(Created, 12, 2) as dec) as create_hour, 
          Created, 
          
          cast(Id1 as dec) as Id2, 

          -- MySQL engine 8.0以後才有row_number() 我們現在是5.7.33
          -- see: https://www.mysqltutorial.org/mysql-row_number/
          -- for how to emulate row_number()

          -- 下面這句壞
          -- row_number() over(partition by Error order by Id2) row_id, 
          

          @row_id_ERR := CASE  -- if `Error` (or the col you want to partition) changes, reset row_id to 1, else row_id++
            WHEN @tmp_Error_ERR = Error 
            THEN @row_id_ERR + 1 
            ELSE 1 
          END AS row_id, 

          @tmp_Error_ERR := Error Error,
          Status 
        from 
          `checks_ddspasyntheticsalerts`
        order by 
          Error, cast(Id1 as dec)