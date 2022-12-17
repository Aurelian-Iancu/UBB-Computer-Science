package model.value;

import model.type.BoolType;
import model.type.Type;

public class BoolValue implements Value{
    private final boolean val;

    public BoolValue(boolean val) {
        this.val = val;
    }

    public boolean getVal(){
        return this.val;
    }

    @Override
    public Type getType() {
        return new BoolType();
    }

    @Override
    public Value deepCopy() {
        return new BoolValue(val);
    }

    @Override
    public String toString(){
        return this.val ? "true" : "false";
    }
}
