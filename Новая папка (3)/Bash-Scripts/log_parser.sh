#!/bin/bash
grep "ERROR" app.log > errors.txt
echo "Найдено $(wc -l < errors.txt) ошибок"
