package model.type;

import model.value.IntValue;
import model.value.Value;

public class IntType implements Type{
    @Override
    public String toString(){
        return "int";
    }

    @Override
    public boolean equals(Type anotherType) {
        if(anotherType instanceof IntType)
            return true;
        else
            return false;
    }

    @Override
    public Value defaultValue() {
        return new IntValue(0);
    }

}
