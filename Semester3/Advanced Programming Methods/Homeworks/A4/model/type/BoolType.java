package model.type;

import model.value.BoolValue;
import model.value.Value;

public class BoolType implements Type{

    @Override
    public String toString() {
        return "boolean";
    }

    @Override
    public boolean equals(Type anotherType) {
        if(anotherType instanceof BoolType)
            return true;
        else
            return false;
    }

    @Override
    public Value defaultValue() {
        return new BoolValue(false);
    }


}
