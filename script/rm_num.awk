{
    if( $1 ~ /[0-9]$|[0-9]{2-10}$/){ # remove date
        next;
    }
    print $0;
}
