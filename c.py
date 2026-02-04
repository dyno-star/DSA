ll
for(int i = 1, i <= n, i++){
    for (int j = 1, j<= i, j++){
        fputs("*", stdout)
    }
    fputs("\n", stdout)
}

ul
for(int i = n; i >= 1; i--){
     for (int j = 1, j<= i, j++){
        fputs("*", stdout)
    }
    fputs("\n", stdout)
}

lr
(for i = 1, i <= n, i ++){
    for(int j = 1, j <= n-i, j++){
        fputs(" ", stdout)
    }

    for (int j = 1, j<= i, j++){
        fputs("*", stdout)
    }
    fputs("\n", stdout)
}

ur
for(i = 1, i >= 1, i--){
    for(int j = 1, j <= n -1, j++){
        fputs(" ", stdout)
    }
     for (int j = 1, j<= i, j++){
        fputs("*", stdout)
    }
    fputs("\n", stdout)
}


